from flask_restful import Resource, reqparse
from models import db, Tutor, Pet, TutorSchema, PetSchema
from models import TutorPetSchema

# Controller dos tutores
class TutorResource(Resource):
    # FindAll ou FindOne
    def get(self, tutor_id=None): 
        # FindAll
        if tutor_id is None:
            tutors = Tutor.query.all()
            return TutorSchema(many=True).dump(tutors), 200
        
        # FindOne
        tutor = Tutor.query.get(tutor_id)
        if tutor is None:
            return {"message": "O tutor especificado não existe"}, 404
        
        # Junta o tutor e os pets
        tutor_schema = TutorPetSchema()
        return tutor_schema.dump(tutor), 200
    
    # Create
    def post(self, tutor_id=None):
        # Estrutura esperada dos dados
        parse = reqparse.RequestParser()
        parse.add_argument('nome_tutor', type=str, required=True)
        
        # Parse dos dados
        try:
            args = parse.parse_args()
            novo_tutor = Tutor(nome=args['nome_tutor'])
        except Exception as e:
            return {"message": str(e)}, 400
        
        # Salva no DB
        db.session.add(novo_tutor)
        db.session.commit()
        
        return TutorSchema().dump(novo_tutor), 201
    
    # Update
    def put(self, tutor_id=None):
        # Estrutura dos dados
        parse = reqparse.RequestParser()
        parse.add_argument('nome_tutor', type=str, required=True)
        
        # Parse dos dados
        try:
            args = parse.parse_args()
            novo_tutor = Tutor(nome=args['nome_tutor'])
        except:
            return {"message": "Dados inválidos"}, 400
        
        # Busca o tutor do DB
        tutor = Tutor.query.get(tutor_id)
        
        # Caso não haja tutor, retorna erro
        if tutor is None:
            return {"message": "Tutor não encontrado"}, 404
        
        # Modifica o tutor
        tutor.nome = args['nome_tutor']
        db.session.commit()
        
        return TutorSchema().dump(tutor), 200
    
    # Delete
    def delete(self, tutor_id=None):
        # Busca o tutor do DB
        tutor = Tutor.query.get(tutor_id)
        
        # Caso não haja tutor, retorna erro
        if tutor is None:
            return {"message": "Tutor não encontrado"}, 404
        
        # Deleta todos os pets do tutor
        for pet in tutor.pets:
            db.session.delete(pet)
        
        # Deleta o tutor
        db.session.delete(tutor)
        db.session.commit()
        
        return {"message": "Tutor deletado"}, 200

    
class PetResource(Resource):
    # FindAll ou FindOne
    def get(self, pet_id=None):
        # FindAll
        if pet_id is None:
            pets = Pet.query.all()
            return PetSchema(many=True).dump(pets), 200
        
        # FindOne
        pet = Pet.query.get(pet_id)
        if pet is None:
            return {"message": "Pet não encontrado"}, 404
        
        return PetSchema().dump(pet), 200
    
    def post(self, pet_id=None):
        # Estrutura dos dados
        parse = reqparse.RequestParser()
        parse.add_argument('nome_pet', type=str, required=True)
        parse.add_argument('tutor_id', type=int, required=True)
        
        # Parse dos dados
        try:
            args = parse.parse_args()
            novo_pet = Pet(nome=args['nome_pet'], tutor_id=args['tutor_id'])
            
            # Salva no DB
            db.session.add(novo_pet)
            db.session.commit()
            return PetSchema().dump(novo_pet), 201
        except:
            return {"message": "Dados inválidos"}, 400
        
    
    def put(self, pet_id=None):
        # Estrutura dos dados
        parse = reqparse.RequestParser()
        parse.add_argument('nome_pet', type=str, required=True)
        parse.add_argument('tutor_id', type=int, required=True)
        
        # Parse dos dados
        try:
            args = parse.parse_args()
        except:
            return {"message": "Dados inválidos"}, 400
        
        # Busca o pet no DB
        pet = Pet.query.get(pet_id)
        if pet is None:
            return {"message": "Pet não encontrado"}, 404
        
        # Modifica a entrada do pet
        pet.nome = args['nome_pet']
        pet.tutor_id = args['tutor_id']
        db.session.commit()
        return PetSchema().dump(pet), 200
    
    def delete(self, pet_id=None):
        # Busca o pet no DB
        pet = Pet.query.get(pet_id)
        
        # Se nao houver pet, retorna erro
        if pet is None:
            return {"message": "Pet não encontrado"}, 404
        
        # Deleta o pet
        db.session.delete(pet)
        db.session.commit()
        return {"message": "Pet deletado"}, 200
