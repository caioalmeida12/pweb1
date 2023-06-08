from flask import render_template, request, redirect, url_for

def findAll():
    return render_template('../paginas/produtos.html')

def findOne(id):
    return render_template('../paginas/ver-produto.html')

def create(form):
    # Caso seja uma requisição POST
    if form is not None:
        return "POST produto"
    
    return render_template('../paginas/cadastro-produtos.html')

def update(id, form):
    return render_template('../paginas/editar-produto.html')

def delete(id):
    return render_template('../paginas/excluir-produto.html')
