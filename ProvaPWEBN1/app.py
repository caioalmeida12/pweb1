from flask import Flask, render_template, request
from controllers import funcionariosController

app = Flask(__name__, template_folder="views")
dbFuncionarios = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/funcionarios")
def funcionarios():
    return funcionariosController.get()

@app.route("/ver-funcionario/", methods=["GET"])
@app.route("/ver-funcionario/<id>", methods=["GET", "POST"])
def ver_funcionario(id=None):
    if id is None:
        return funcionariosController.form("/ver-funcionario")
    
    return funcionariosController.findOne(id)

@app.route("/cadastrar-funcionario", methods=["GET", "POST"])
def cadastrar_funcionario():
    if request.method == "GET":
        return funcionariosController.form("/cadastrar-funcionario")
    
    return funcionariosController.create(request.form)

@app.route("/editar-funcionario/", methods=["GET"])
@app.route("/editar-funcionario/<id>", methods=["GET", "POST"])
def editar_funcionario(id=None):
    if request.method == "GET":
        return funcionariosController.form("/editar-funcionario")
    
    return funcionariosController.update(id, request.form)

@app.route("/deletar-funcionario/", methods=["GET"])
@app.route("/deletar-funcionario/<id>", methods=["GET", "POST"])
def deletar_funcionario(id=None):
    if request.method == "GET":
        return funcionariosController.form("/deletar-funcionario")
    
    return funcionariosController.delete(id)

if __name__ == '__main__':
    app.run(port=5000,debug=True)