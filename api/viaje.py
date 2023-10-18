from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viaje import Viaje, ViajesSchema

ruta_viajes = Blueprint("ruta_viajes", __name__)

viaje_schema = ViajesSchema()
viaje_schema = ViajesSchema(many=True)

@ruta_viajes.route('/viajes', methods=['GET'])
def viaje():
    resultall = Viaje.query.all() #Select * from Viaje
    resultado_viaje= viaje_schema.dump(resultall)
    return jsonify(resultado_viaje)

@ruta_viajes.route('/saveviaje', methods=['POST'])
def save():
    solicitudid = request.json['solicitudid']
    horainicio = request.json['horainicio']
    horafinalizacion = request.json['horafinalizacion']
    ruta = request.json['ruta']
    new_viaje = Viaje(solicitudid, horainicio, horafinalizacion, ruta)
    db.session.add(new_viaje)
    db.session.commit()    
    return "datos guardado con exito"
    
@ruta_viajes.route('/updateviaje', methods=['PUT'])
def update():
    id = request.json['id']
    solicitudid = request.json['solicitudid']
    horainicio = request.json['horainicio']
    horafinalizacion = request.json['horafinalizacion']
    ruta = request.json['ruta']
    viaje = Viaje.query.get(id)   
    if viaje :
        print(viaje) 
        viaje.solicitudid = solicitudid
        viaje.horainicio = horainicio
        viaje.horafinalizacion = horafinalizacion
        viaje.ruta = ruta
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_viajes.route('/deleteviaje/<id>', methods=['GET'])
def delete(id):
    viaje = Viaje.query.get(id)
    db.session.delete(viaje)
    db.session.commit()
    return jsonify(viaje_schema.dump(viaje))