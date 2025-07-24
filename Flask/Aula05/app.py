# Introdução ao Flask - Framework Python para aplicações WEB
# Requisições WEB -> GET e POST
# instalação do Flask -> pip install flask

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Enviando variaveis para o HTML
    nome = 'João'
    idade = 30
    email = 'joao@gmail.com'
    return render_template('index.html',name = nome,idade = idade,email = email)

@app.route('/dicionarios')
def dicionarios():
    # Enviando dicionarios para o html
    usuario = {
        "nome": "João",
        "idade": 20,
        "email":"joao@gmail.com"
    }
    return render_template('dicionarios.html', usuario = usuario)

@app.route('/condicionais')
def condicionais():
    nota = 3
    logado = False
    usuario = {
        "nome": "João",
        "idade": 20,
        "email":"joao@gmail.com"
    }

    return render_template('condicionais.html',logado = logado, usuario = usuario,nota = nota)

@app.route('/listas')
def listas():
    listaUsuarios = ['Maria', 'João','André','Sara']

    return render_template('listas.html',listaUsuarios = listaUsuarios)

if __name__ == '__main__':
    app.run(debug=True)




