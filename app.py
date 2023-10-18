from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.pasajero import Pasajero, ruta_pasajeros
from api.vehiculo import Vehiculo, ruta_vehiculos
from api.solicitud import Solicitud, ruta_solicitudes
from api.viaje import Viaje, ruta_viajes
from api.pago import Pago, ruta_pagos
from api.conductor import Conductor, ruta_conductores

# tablas independientes
app.register_blueprint(ruta_pasajeros,url_prefix = '/api')
app.register_blueprint(ruta_vehiculos, url_prefix = '/api')
app.register_blueprint(ruta_conductores, url_prefix = '/api')
# tablas dependientes
app.register_blueprint(ruta_solicitudes, url_prefix = '/api')
app.register_blueprint(ruta_viajes, url_prefix = '/api')
app.register_blueprint(ruta_pagos, url_prefix = '/api')

@app.route('/')
def index():
    return "Hola Mundo"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')