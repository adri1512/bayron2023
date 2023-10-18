from config.db import  db, ma, app

class Pasajero(db.Model):
    __tablename__ = "tblpasajero"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    cedula = db.Column(db.String(50))
    telefono = db.Column(db.String(50))

    def __init__(self, nombre, cedula, telefono) :
       self.nombre = nombre
       self.cedula = cedula 
       self.telefono = telefono

with app.app_context():
    db.create_all()

class PasajerosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'cedula', 'telefono')