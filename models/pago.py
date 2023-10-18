from config.db import  db, ma, app

class Pago(db.Model):
    __tablename__ = "tblpago"

    id = db.Column(db.Integer, primary_key=True)
    viajeid = db.Column(db.Integer, db.ForeignKey('tblviaje.id'))
    montopagado = db.Column(db.Float)
    metodopago = db.Column(db.String(50))
    estadopago = db.Column(db.String(50))

    def __init__(self, viajeid, montopagado, metodopago, estadopago):
        self.viajeid = viajeid
        self.montopagado = montopagado
        self.metodopago = metodopago
        self.estadopago = estadopago

with app.app_context():
    db.create_all()

class PagosSchema(ma.Schema):
    class Meta:
        fields = ('id','viajeid', 'montopagado', 'metodopago', 'estadopago')