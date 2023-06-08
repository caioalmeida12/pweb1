from flask import redirect, render_template
from models.produtoModel import Produto

def get():
    return render_template("produtos.html", produtos=Produto.findAll())

def findOne(id=None):
    return render_template("ver_produto.html", produto=Produto.findOne(id))
    
def create(form=None):
    # GET
    if form is None:
        return render_template("create.html")
    
    # POST
    produto = Produto(form["id"], form["nome"], form["descricao"], form["preco"])  
    
    if produto:
        return redirect("/ver-produto/" + form["id"])    
    
    return str("Erro ao criar produto ->" + produto)

def update(id=None, form=None):
    # GET
    if id is None or form is None:
        return render_template("update.html")
    
    # POST
    produto = Produto.findOne(id)
    
    if produto is None:
        return "Produto não encontrado -> " + id
    
    produto.nome = form["nome"]
    produto.descricao = form["descricao"]
    produto.preco = form["preco"]
    
    return redirect("/ver-produto/" + id)

def delete(id=None):
    if id is None:
        return "ID não informado"
    
    Produto.delete(id)
    return redirect("/produtos")
    
    
