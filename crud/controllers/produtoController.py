from flask import redirect, render_template
from models.produtoModel import Produto

def findAll():
    return render_template('paginas/produtos.html', produtos = Produto.findAll());

def findOne(id):
    return render_template('paginas/ver-produto.html', produto = Produto.findOne(id));

def create(form):
    # Caso seja uma requisição GET, retorna o formulário
    if form is None:
        return render_template('paginas/cadastro-produtos.html')
        
    # Caso seja uma requisição POST, cria o produto
    produto = Produto(form['id'], form['nome'], form['descricao'], form['preco'])
    return redirect('/ver-produto/' + str(produto.id))

def update(id, form):
    return render_template('../paginas/editar-produto.html')

def delete(id):
    return render_template('../paginas/excluir-produto.html')
