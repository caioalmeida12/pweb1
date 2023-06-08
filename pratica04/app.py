from flask import Flask, request
from controllers import indexController, produtoController

app = Flask(__name__, template_folder="views")
dbProdutos = []

@app.route('/')
def index():
    return indexController.get()

@app.route('/produtos/')
def produtos():
    return produtoController.findAll()
    
@app.route('/cadastro-produtos', methods=["GET", "POST"])
def cadastroprodutos():
    if request.method == "POST":
        return produtoController.create(request.form)
    
    return produtoController.create(None)

@app.route('/ver-produto/<id>')
def verproduto(id):
    return produtoController.findOne(id)

@app.route('/editar-produto/<id>', methods=["GET", "POST"])
def editarproduto(id):
    if request.method == "POST":
        return produtoController.update(id, request.form)
    
    return produtoController.update(id, None)

@app.route('/excluir-produto/<id>', methods=["GET", "POST"])
def excluirproduto(id):
    return produtoController.delete(id)

if __name__ == '__main__':
    app.run(debug = True)