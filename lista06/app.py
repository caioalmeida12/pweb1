from flask import Flask, render_template, request, redirect, url_for
from utils import valida_cadastro

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    # Método POST
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == 'admin' and senha == 'admin':
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('index'))
    
    # Método GET
    sucesso = request.args.get("sucesso")
    return render_template('login.html', sucesso=sucesso)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Caso exista alguma mensagem de erro na url, a salva
    erro = request.args.get("erro")
    
    # Houve um erro no cadastro
    if erro != "":
        data = request.form
        return render_template('cadastrar.html', erro=erro, form=data)        
    
    # Não houve nenhuma tentativa de cadastro ainda
    return render_template('cadastrar.html', erro=None, form=None)        
        
@app.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confsenha = request.form['confsenha']
    
    msg = valida_cadastro(nome, email, senha, confsenha)
    
    # Caso não haja erro, redireciona para a página de login
    if msg is None:
       return redirect(url_for('login', sucesso="Você foi cadastrado com sucesso! Faça login para continuar." )) 
       
    # Caso haja erro, redireciona para a página de cadastro
    return redirect(url_for('signup', erro=msg))

@app.route('/admin')
def admin():
    return render_template('admin.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)   