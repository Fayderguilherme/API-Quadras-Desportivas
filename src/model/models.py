#O seu 'M' - As classes do banco de dados
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classes

class Quadras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    

class Inquilino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class Reservas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    horario = db.Column(db.Time)
    quadras_id = db.Column(db.Integer, db.ForeignKey('quadras.id'), nullable=False)
    inquilino_id = db.Column(db.Integer, db.ForeignKey('inquilino.id'), nullable=False)








