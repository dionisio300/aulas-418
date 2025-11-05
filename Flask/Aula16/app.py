from flask import Flask, render_template, url_for, redirect, request

import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        idade = request.form.get('idade')
        linguagem = request.form.getlist('linguagem')
        vaga = request.form.get('vaga')

        print(nome,email,senha,idade,linguagem,vaga)
        return render_template('index.html')


@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')


@app.route('/pagina3')
def pagina3Todos():
    url = f'https://fakestoreapi.com/products'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        erro = False
        print(dados)
        return render_template('pagina3Todos.html',erro=erro,dados=dados)
    else:
        erro = True
        return render_template('pagina3Todos.html',erro=erro)


@app.route('/pagina3/<int:id>')
def pagina3(id):

    url = f'https://fakestoreapi.com/products/{id}'

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados['image'])
        erro = False
        print(dados)
        return render_template('pagina3.html',dados=dados,erro=erro)
    else:
        erro = True
        return render_template('pagina3.html',erro=erro)


app.run(debug=True)