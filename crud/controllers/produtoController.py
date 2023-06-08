from flask import jsonify, redirect, render_template
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
    # Caso seja uma requisição GET, retorna o formulário
    if form is None:
        return render_template('paginas/editar-produto.html')
    
    # Caso seja uma requisição POST, atualiza o produto
    produto = Produto.findOne(id)
        
    # Redireciona para o formulario caso não exista o produto
    if produto is None:
        return jsonify({'erro': 'Produto não encontrado'})
    
    produto.nome = form['nome']
    produto.descricao = form['descricao']
    produto.preco = form['preco']
    
    return redirect('/ver-produto/' + str(produto.id))

def delete(id):
    #  Caso seja uma requisição GET, retorna o formulário
    if id == "None":
        return render_template('paginas/excluir-produto.html') 

    # Caso seja uma requisição POST, deleta o produto
    produto = Produto.delete(id)
        
    # Redireciona para o formulario caso não exista o produto
    if produto is None:
        return jsonify({'erro': 'Produto não encontrado'})
    
    
    return redirect('/produtos/')
