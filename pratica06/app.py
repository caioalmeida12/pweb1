from flask import Flask
from flask_restful import Api
from models import db, ma
from resources import TutorResource,PetResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memory'

api = Api(app)
db.init_app(app)
ma.init_app(app)

api.add_resource(TutorResource,'/tutor/<int:tutor_id>', '/tutor/')
api.add_resource(PetResource,'/pet/<int:pet_id>', '/pet/')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)