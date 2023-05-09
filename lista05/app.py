from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carrinho/<item>')
def carrinho(item):
    return render_template('carrinho.html', item=item)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")