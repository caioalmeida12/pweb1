from app import dbFuncionarios

class Funcionario:
    def __init__(self, id="nao informado", nome="nao informado", cargo="nao informado"):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        dbFuncionarios.append(self)
        
    def findAll():
        return str(dbFuncionarios)
    
    def findOne(id):
        for funcionario in dbFuncionarios:
            if (funcionario.id == id):
                return funcionario
        return False
    
    def delete(id):
        for funcionario in dbFuncionarios:
            if (funcionario.id == id):
                dbFuncionarios.remove(funcionario)
                return True
        return False
    
    def __repr__(self):
        return str(self.__dict__)