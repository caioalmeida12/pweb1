from flask import Flask, request
from controllers import indexController, productController

app = Flask(__name__, template_folder="views")
dbProducts = []

@app.route("/")
def index():
    return indexController.index()

@app.route("/produtos")
def findAll():
    return productController.findAll()

@app.route("/ver-produto", methods=["GET"])
@app.route("/ver-produto/<id>", methods=["GET", "POST"])
def findOne(id=None):
    if request.method == "GET":
        return productController.get("ver-produto")
    
    return productController.findOne(id)

@app.route("/cadastro-produtos", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return productController.get("cadastro-produtos")
        
    return productController.create(request.form)

@app.route("/editar-produto/", methods=["GET"])
@app.route("/editar-produto/<id>", methods=["GET", "POST"])
def update(id=None):
    if request.method == "GET":
        return productController.get("editar-produto")
    
    return productController.update(id, request.form)

@app.route("/excluir-produto")
@app.route("/excluir-produto/<id>", methods=["GET", "POST"])
def delete(id=None):
    if request.method == "GET":
        return productController.get("excluir-produto")
    
    return productController.delete(id)

if __name__=="__main__":
    app.run(debug=True)