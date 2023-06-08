from app import dbProdutos;

class Produto():
    def __init__(self, id, nome, descricao, preco):
        self.id = id;
        self.nome = nome;
        self.descricao = descricao;
        self.preco = preco;
        self.save()
        
    def save(self):
        if self.validate():
            dbProdutos.append(self)
        return False
    
    def validate(self):
        if (not (self.nome and self.descricao and self.id and self.preco)):
            return False
        return True
    
    def findAll():
        return dbProdutos
    
    def findOne(id=None):
        if id is not None:
            for produto in dbProdutos:
                if produto.id == id:
                    return produto
                return False
            
        return None
    
    def delete(id=None):
        if id is not None:
            for produto in dbProdutos:
                if produto.id == id:
                    dbProdutos.remove(produto)
        
        return "ID inexistente"
    
    def __repr__(self):
        return str(self.__dict__)