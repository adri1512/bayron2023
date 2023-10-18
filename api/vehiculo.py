from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import Vehiculo, VehiculosSchema

ruta_vehiculos = Blueprint("ruta_vehiculos", __name__)

vehiculo_schema = VehiculosSchema()
vehiculos_schema = VehiculosSchema(many=True)

@ruta_vehiculos.route('/vehiculos', methods=['GET'])
def vehiculo():
    resultall = Vehiculo.query.all() #Select * from Vehiculo
    resultado_vehiculo= vehiculos_schema.dump(resultall)
    return jsonify(resultado_vehiculo)

@ruta_vehiculos.route('/savevehiculo', methods=['POST'])
def save():
    placa = request.json['placa']
    marca = request.json['marca']
    capacidad = request.json['capacidad']
    estado = request.json['estado']
    new_vehiculo = Vehiculo(placa, marca, capacidad, estado)
    db.session.add(new_vehiculo)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_vehiculos.route('/updatevehiculo', methods=['PUT'])
def update():
    id = request.json['id']
    placa = request.json['placa']
    marca = request.json['marca']
    capacidad = request.json['capacidad']
    estado = request.json['estado']
    vehiculo = Vehiculo.query.get(id)   
    if vehiculo :
        print(vehiculo) 
        vehiculo.placa = placa
        vehiculo.marca = marca
        vehiculo.capacidad = capacidad
        vehiculo.estado = estado
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_vehiculos.route('/deletevehiculo/<id>', methods=['GET'])
def delete(id):
    vehiculo = Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify(vehiculo_schema.dump(vehiculo))