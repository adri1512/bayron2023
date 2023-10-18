from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pasajero import Pasajero, PasajerosSchema

ruta_pasajeros = Blueprint("ruta_pasajeros", __name__)

pasajero_schema = PasajerosSchema()
pasajeros_schema = PasajerosSchema(many=True)

@ruta_pasajeros.route('/pasajeros', methods=['GET'])
def pasajero():
    resultall = Pasajero.query.all() #Select * from Pasajero
    resultado_pasajero= pasajeros_schema.dump(resultall)
    return jsonify(resultado_pasajero)

@ruta_pasajeros.route('/savepasajero', methods=['POST'])
def save():
    nombre = request.json['nombre']
    cedula = request.json['cedula']
    telefono = request.json['telefono']
    new_pasajero = Pasajero(nombre, cedula, telefono)
    db.session.add(new_pasajero)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_pasajeros.route('/updatepasajero', methods=['PUT'])
def update():
    id = request.json['id']
    nombre = request.json['nombre']
    cedula = request.json['cedula']
    telefono = request.json['telefono']
    pasajero = Pasajero.query.get(id)   
    if pasajero :
        print(pasajero) 
        pasajero.nombre = nombre
        pasajero.cedula = cedula
        pasajero.telefono = telefono
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_pasajeros.route('/deletepasajero/<id>', methods=['GET'])
def delete(id):
    pasajero = Pasajero.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(pasajero_schema.dump(pasajero))