from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pago import Pago, PagosSchema

ruta_pagos = Blueprint("ruta_pagos", __name__)

pago_schema = PagosSchema()
pagos_schema = PagosSchema(many=True)

@ruta_pagos.route('/pagos', methods=['GET'])
def pago():
    resultall = Pago.query.all() #Select * from Pago
    resultado_pago= pagos_schema.dump(resultall)
    return jsonify(resultado_pago)

@ruta_pagos.route('/savepago', methods=['POST'])
def save():
    viajeid = request.json['viajeid']
    montopagado = request.json['montopagado']
    metodopago = request.json['metodopago']
    estadopago = request.json['estadopago']
    new_pago = Pago(viajeid, montopagado, metodopago, estadopago)
    db.session.add(new_pago)
    db.session.commit()    
    return "datos guardado con exito"

@ruta_pagos.route('/updatepasajero', methods=['PUT'])
def update():
    id = request.json['id']
    viajeid = request.json['viajeid']
    montopagado = request.json['montopagado']
    metodopago = request.json['metodopago']
    estadopago = request.json['estadopago']
    pago = Pago.query.get(id)   
    if pago :
        print(pago) 
        pago.viajeid = viajeid
        pago.montopagado = montopagado
        pago.metodopago = metodopago
        pago.estadopago = estadopago
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"

@ruta_pagos.route('/deletepago/<id>', methods=['GET'])
def delete(id):
    pago = Pago.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(pago_schema.dump(pago))