from config.db import  db, ma, app

class Viaje(db.Model):
    __tablename__ = "tblviaje"

    id = db.Column(db.Integer, primary_key=True)
    solicitudid = db.Column(db.Integer, db.ForeignKey('tblsolicitud.id'))
    horainicio = db.Column(db.String(50))
    horafinalizacion = db.Column(db.String(50))
    ruta = db.Column(db.String(100))

    def __init__(self, solicitudid, horainicio, horafinalizacion, ruta):
        self.solicitudid = solicitudid
        self.horainicio = horainicio
        self.horafinalizacion = horafinalizacion
        self.ruta = ruta

class ViajesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'solicitudid', 'horainicio', 'horafinalizacion', 'ruta')
