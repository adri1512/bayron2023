from config.db import  db, ma, app

class Solicitud(db.Model):
    __tablename__ = "tblsolicitud"

    id = db.Column(db.Integer, primary_key=True)
    origen = db.Column(db.String(50))
    destino = db.Column(db.String(50))
    preferencias = db.Column(db.String(50))
    capacidaddeseada = db.Column(db.String(50))
    pasajeroid = db.Column(db.Integer, db.ForeignKey('tblpasajero.id'))
    vehiculoid = db.Column(db.Integer, db.ForeignKey('tblvehiculo.id'))
    
    def __init__(self, origen, destino, preferencias, capacidaddeseada, pasajeroid, vehiculoid):
        self.origen = origen
        self.destino = destino
        self.preferencias = preferencias
        self.capacidaddeseada = capacidaddeseada
        self.pasajeroid = pasajeroid
        self.vehiculoid = vehiculoid

with app.app_context():
    db.create_all()

class SolicitudesSchema(ma.Schema):
    class Meta:
        fields = ('id','origen', 'destino', 'preferencias', 'capacidaddeseada', 'pasajeroid', 'vehiculoid')