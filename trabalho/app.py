from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

dbTimes = []

class Time:
    def __init__(self, nome, cidade):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.jogadores = []
        self.resultados = []
    
    def adicionar_jogador(self, jogador):
        self.jogadores.append(str(jogador))
        
    def adicionar_resultado(self, resultado):
        self.resultados.append(resultado)
    
    def __str__(self):
        return self.id, self.nome, self.cidade, self.jogadores

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        
    def __str__(self):
        return str(self.nome) + " - " + str(self.posicao)
    
class Resultado:
    def __init__(self, id_time1, id_time2, gols_time1, gols_time2):
        
        # use the id_time to get the name of the team and save as attributes
        self.time1 = dbTimes[id_time1 - 1].nome
        self.time2 = dbTimes[id_time2 - 1].nome
        self.gols_time1 = gols_time1
        self.gols_time2 = gols_time2
        
        # save the Resultado in each teams' list of resultados
        dbTimes[id_time1 - 1].adicionar_resultado(self)
        dbTimes[id_time2 - 1].adicionar_resultado(self)
         
    def __str__(self):
        return str(self.time1) + " " + str(self.gols_time1) + " x " + str(self.gols_time2) + " " + str(self.time2)
        

@app.route('/')
def index():
    return render_template('paginas/index.html', dbTimes=dbTimes)

@app.route('/cadastro/time')
def cadastrotime():
    return render_template('paginas/cadastrotime.html', dbTimes=dbTimes)

@app.route('/cadastro/jogador')
def cadastrojogador():
    return render_template('paginas/cadastrojogador.html', dbTimes=dbTimes)

@app.route('/cadastro/resultado')
def cadastroresultado():
    return render_template('paginas/cadastroresultado.html', dbTimes=dbTimes)

@app.route('/cadastro/time', methods=['POST'])
def cadastrotime_post():
    timeTemp = Time(request.form['nome_time'], request.form['cidade_time'])
    timeTemp.id = len(dbTimes) + 1
    dbTimes.append(timeTemp)
    return render_template('paginas/cadastrotime.html', dbTimes=dbTimes)

@app.route('/cadastro/jogador', methods=['POST'])
def cadastrojogador_post():
    jogadorTemp = Jogador(request.form['nome_jogador'], request.form['posicao_jogador'])
    dbTimes[int(request.form['id_time']) - 1].adicionar_jogador(jogadorTemp)
    return render_template('paginas/cadastrojogador.html', dbTimes=dbTimes)

@app.route('/cadastro/resultado', methods=['POST'])
def cadastroresultado_post():
    resultadoTemp = Resultado(int(request.form['id_time1']), int(request.form['id_time2']), int(request.form['gols_time1']), int(request.form['gols_time2']))
    return render_template('paginas/cadastroresultado.html', dbTimes=dbTimes)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")