from flask import Flask
from controllers import indexController, produtoController

app = Flask(__name__, template_folder="views")
dbProdutos = []

@app.route('/')
def index():
    return indexController.get()

@app.route('/produtos/')
def produtos():
    return produtoController.findAll()
    
# @app.route('/cadastro-produtos', methods=["GET", "POST"])
# def cadastroprodutos():
#     produtoController.create(request.form)
    
# @app.route('/ver-produto/<id>')
# def verproduto(id):
#     return render_template('paginas/ver-produto.html')

# @app.route('/editar-produto/<id>')
# def editarproduto(id):
#     return render_template('paginas/editar-produto.html')

# @app.route('/excluir-produto/<id>')
# def excluirproduto(id):
#     return render_template('paginas/excluir-produto.html')

if __name__ == '__main__':
    app.run(debug = True)