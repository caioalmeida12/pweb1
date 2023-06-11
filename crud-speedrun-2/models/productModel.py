from app import dbProducts

class Produto:
    def __init__(self, id="nao informado", nome="nao informado", descricao="nao informado", preco="nao informado"):
        self.id = id;
        self.nome = nome;
        self.descricao = descricao;
        self.preco = preco;
        dbProducts.append(self)
    
    def findAll():
        return str(dbProducts)
    
    def findOne(id):
        for product in dbProducts:
            if (product.id == id):
                return product
        return False
    
    def delete(id):
        for product in dbProducts:
            if (product.id == id):
                dbProducts.remove(product)
                return True
        return False
    
    def __repr__(self):
        return str(self.__dict__)