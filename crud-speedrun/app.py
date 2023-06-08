from flask import Flask, request
from controllers import indexController, produtoController

app = Flask(__name__, template_folder="views");
dbProdutos = [];

@app.route("/")
def index():
    return indexController.get()

@app.route("/produtos")
def produtos():
    return produtoController.get()

@app.route("/cadastrar-produtos", methods=["GET", "POST"])
def cadastrar_produtos():
    if request.method == "POST":
        return produtoController.create(request.form)
    
    return produtoController.create(None)

@app.route("/ver-produto/<id>")
def ver_produto(id):
    return produtoController.findOne(id)

@app.route("/editar-produto/", methods=["GET"])
@app.route("/editar-produto/<id>", methods=["GET", "POST"])
def editar_produto(id=None):
    if request.method == "POST":
        return produtoController.update(id, request.form)
    
    return produtoController.update(id, None)

@app.route("/excluir-produto/<id>")
def excluir_produto(id):
    return produtoController.delete(id)

if __name__ == '__main__':
    app.run(debug = True)