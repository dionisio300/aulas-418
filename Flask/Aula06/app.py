from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    # Enviar variáveis simples
    userName = 'João'

    # Enviando Dicionários
    usuario = {
        "nome": 'João',
        "idade":25,
        "email":"joão@gmail.com",
        "senha":"senha123"
    }

    # Enviando Listas
    linguagensProgramacao = ['Python','JavaScript','C','C++','Java']

    # enviando booleano
    logado = True

    return render_template('index.html',userName = userName,user = usuario,linguagensProgramacao = linguagensProgramacao,logado = logado)

@app.route('/pagina1', methods = ['GET','POST'])
def pagina1():

    if request.method == 'GET':
        return render_template('pagina1.html')
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        area = request.form.get('area')
        
        return render_template('dadosUsuario.html',nome = nome, idade = idade, area = area)


@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')

app.run(debug=True)