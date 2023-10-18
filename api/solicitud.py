from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.solicitud import Solicitud, SolicitudesSchema
from models.vehiculo import Vehiculo

ruta_solicitudes = Blueprint("ruta_solicitudes", __name__)

solicitud_schema = SolicitudesSchema()
solicitudes_schema = SolicitudesSchema(many=True)

@ruta_solicitudes.route('/solicitudes', methods=['GET'])
def solicitud():
    resultall = Solicitud.query.all() #Select * from Pasajero
    resultado_solicitud= solicitudes_schema.dump(resultall)
    return jsonify(resultado_solicitud)

@ruta_solicitudes.route('/savesolicitud', methods=['POST'])
def save():
    origen = request.json['origen']
    destino = request.json['destino']
    preferencias = request.json['preferencias']
    capacidaddeseada = request.json['capacidaddeseada']
    pasajeroid = request.json['pasajeroid']
    vehiculos_estado = Vehiculo.query.filter(Vehiculo.disponibilidad == True).all()
    if vehiculos_estado:
        asignado = asignar(vehiculos_estado, capacidaddeseada)
        if asignado is not None:
            asignado.disponibilidad = False
            new_solicitud = Solicitud(origen, destino, preferencias, pasajeroid, asignado.id)
            db.session.add(new_solicitud)
            db.session.commit()    
            return "datos guardado con exito"
    else:
        return "error"

def asignar(vehiculos_estado, capacidaddeseada):
    for vehiculo in vehiculos_estado:
    # Si no se encontró un vehículo con la capacidad, asigna cualquier vehículo disponible
        if vehiculo.disponibilidad and vehiculo.capacidad == capacidaddeseada:
            return vehiculo
    for vehiculo in vehiculos_estado:
        if vehiculo.disponibilidad:
            return vehiculo
    # Si no se encontraron vehículos disponibles, devuelve None
    return None

@ruta_solicitudes.route('/updatesolicitud', methods=['PUT'])
def update():
    id = request.json['id']
    origen = request.json['origen']
    destino = request.json['destino']
    preferencias = request.json['preferencias']
    capacidaddeseada = request.json['capacidaddeseada']
    pasajeroid = request.json['pasajeroid']
    vehiculoid = request.json['vehiculoid']
    solicitud = Solicitud.query.get(id)   
    if solicitud :
        print(solicitud) 
        solicitud.origen = origen
        solicitud.destino = destino
        solicitud.preferencias = preferencias
        solicitud.capacidaddeseada = capacidaddeseada
        solicitud.pasajeroid = pasajeroid
        solicitud.vehiculoid = vehiculoid
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_solicitudes.route('/deletesolicitud/<id>', methods=['GET'])
def delete(id):
    solicitud = Solicitud.query.get(id)
    db.session.delete(solicitud)
    db.session.commit()
    return jsonify(solicitud_schema.dump(solicitud))
