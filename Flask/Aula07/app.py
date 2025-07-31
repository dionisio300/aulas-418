from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)
@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/agendar', methods = ['GET','POST'])
def agendar():

    if request.method == 'GET':
        print('Método GET utilizado')
        return render_template('agendar.html')
    
    elif request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        data = request.form.get('data')
        hora = request.form.get('hora')
        servico = request.form.get('servico')
        
        print(f'Nome: {nome} \nE-mail: {email}\nTelefone: {telefone}\nData: {data}\nHora: {hora}\nServiço: {servico}')
        
        dadosServico = {
            "nome":nome,
            "email":email,
            "telefone":telefone,
            "data":data,
            "hora":hora,
            "servico":servico
        }
        
        return render_template('confirmacaoServico.html',dadosServico = dadosServico)

app.run(debug=True)