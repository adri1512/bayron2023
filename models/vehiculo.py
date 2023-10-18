from config.db import  db, ma, app

class Vehiculo(db.Model):
    __tablename__ = "tblvehiculo"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    capacidad = db.Column(db.Integer)
    estado = db.Column(db.Boolean)

    def __init__(self, placa, marca, capacidad, estado):
        self.placa = placa
        self.marca = marca
        self.capacidad = capacidad
        self.estado = estado

with app.app_context():
    db.create_all()

class VehiculosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'placa', 'marca', 'capacidad', 'estado')
