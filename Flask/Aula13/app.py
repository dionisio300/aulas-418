from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/atividade')
def atividade():
    return render_template('atividade.html')

app.run(debug=True)
