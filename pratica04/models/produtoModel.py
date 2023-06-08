from app import dbProdutos

class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.save()
        
    def __repr__(self):
        return str(self.__dict__)
        
    def validate(self):
        if self.nome is None or self.nome == '':
            return False
        if self.descricao is None or self.descricao == '':
            return False
        if self.preco is None or self.preco == '':
            return False
        return True
    
    def save(self):
        if self.validate():
            dbProdutos.append(self)
            return True
        return False
    
    def findAll():
        return dbProdutos
    
    def findOne(id):
        for produto in dbProdutos:
            if produto.id == id:
                return produto
        return None
    
    def delete(id): 
        for produto in dbProdutos:
            if produto.id == id:
                dbProdutos.remove(produto)
                return produto
        return None