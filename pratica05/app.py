from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from utils import valida_cadastro
import sqlite3

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = '20211035000080'

Session(app)

def init_db():
    conn = sqlite3.connect('users.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    # Método POST
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (usuario, senha))
        existeUsuario = cursor.fetchone()
        
        conn.close()

        if existeUsuario is not None:
            session["nome"] = existeUsuario[1]
            session["email"] = existeUsuario[2]
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('login'))
    
    # Método GET
    sucesso = request.args.get("sucesso")
    
    if session.get("nome"):
        return redirect(url_for("admin"))
    
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
        conn = sqlite3.connect('users.sqlite3')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (username,email, password) VALUES (?,?,?)', (nome, email, senha))
        conn.commit()
        conn.close()
        
        flash('Usuário criado com sucesso!')
        
        return redirect(url_for('login', sucesso="Você foi cadastrado com sucesso! Faça login para continuar." )) 
       
    # Caso haja erro, redireciona para a página de cadastro
    return redirect(url_for('signup', erro=msg))

@app.route('/admin')
def admin():
    if session.get("nome"):
        return render_template('admin.html')
    
    return redirect(url_for("login"))
    
    
if __name__ == '__main__':
    app.run(debug=True)   