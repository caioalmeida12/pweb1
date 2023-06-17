from flask import redirect, render_template 
from models.funcionariosModel import Funcionario

def get():
    return render_template("funcionarios.html", funcionarios=Funcionario.findAll())

def form(formAction):
    return render_template("formulario.html", action=formAction)

def findOne(id):
    funcionario = (Funcionario.findOne(id) or str("Nenhum funcionário encontrado com o ID -> " + str(id)))
    return render_template("funcionarios.html", funcionarios=funcionario)

def create(form):
    funcionario = Funcionario(form["id"], form["nome"], form["cargo"])
    
    if not funcionario:
        return render_template("formulario.html", erro=("Não há funcionarios com esse ID -> " + str(id)))
    
    return redirect("/funcionarios")

def update(id, form):
    funcionario = Funcionario.findOne(id)
    
    if not funcionario:
        return render_template("formulario.html", erro=("Não há funcionarios com esse ID -> " + str(id)))
    
    funcionario.nome = form["nome"]
    funcionario.cargo = form["cargo"]
    
    return redirect("/funcionarios")

def delete(id):
    funcionario = Funcionario.findOne(id)
    
    if not funcionario:
        return render_template("formulario.html", erro=("Não há funcionarios com esse ID -> " + str(id)))
    
    Funcionario.delete(id)
    
    return redirect("/funcionarios")