from flask import redirect, render_template
from models.productModel import Produto

def get(rota):
    return render_template("get.html", rota=rota)

def findAll():
    return Produto.findAll()
    
def findOne(id):
    return str(Produto.findOne(id)) or "Não encontrado";

def create(form):
    Produto(form["id"], form["nome"], form["descricao"], form["preco"])
    return redirect("/produtos")

def update(id, form):
    produto = Produto.findOne(id)
    
    produto.nome = form["nome"]
    produto.descricao = form["descricao"]
    produto.preco = form["preco"]
    
    return redirect("/ver-produto/" + form["id"])
    
def delete(id):
    Produto.delete(id)
    return redirect("/produtos")