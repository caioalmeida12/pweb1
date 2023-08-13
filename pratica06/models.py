from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Modelo do tutor
class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    pets = db.relationship('Pet', backref='tutor', lazy=True)

# Modelo do pet
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable=False)

# Define o schema do tutor
class TutorSchema(ma.Schema):
    class Meta:
        fields = ('id','nome','pets')
        include_fk = True

# Define o schema do pet
class PetSchema(ma.Schema):
    class Meta:
        fields = ('id','nome','tutor_id')
        include_fk = True

# Funciona como uma junção entre o schema do tutor e o do pet
class TutorPetSchema(TutorSchema):
    pets = ma.Nested(PetSchema, many=True)
