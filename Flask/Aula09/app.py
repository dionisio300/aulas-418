from flask import Flask, render_template,request,redirect,url_for
import mysql.connector as my
# Importar o bcrypt para criptografar a senha
import bcrypt



def conectar():
    conexao = my.connect(
        host='localhost',
        user='root',
        password='12341234',
        database='atendimento'
    )
    return conexao

conectar()

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

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('cadastrar.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

       # exemplo de criptografia e verificação da senha
        senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
        print(senha_criptografada)

        senha = senha_criptografada
        # senha = '1234'
        # # Verificando a senha
        # if bcrypt.checkpw(senha.encode('utf-8'), senha_criptografada):
        #     print("Senha correta")
        # else:
        #     print("Senha incorreta")
    
        dtNascimento = request.form.get('dataNascimento')
        cpf = request.form.get('cpf')
        cep = request.form.get('cep')
        tipoUsuario = request.form.get('tipoUsuario')

        try:
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)
            sql = "INSERT INTO usuarios (nome, data_nascimento, cpf, cep, tipo_usuario,senha) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql,(nome,dtNascimento,cpf,cep,tipoUsuario,senha))
            conexao.commit()
            conexao.close()
        except my.Error as erroMy:
            print(f'Erro no mySql {erroMy}')
            erro = True
            return render_template('cadastrar.html',erro = erro)
        except Exception as e:
            print(f'Houve um erro: {e}')
            erro = True
            return render_template('cadastrar.html',erro = erro)


        print(f'Nome: {nome}, Email: {email}, senha: {senha}, Data: {dtNascimento}, CPF: {cpf}, CEP: {cep}, Tipo Usuário: {tipoUsuario}')
        return render_template('cadastrar.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        print(f'email: {email}, senha: {senha}')
        return render_template('login.html')



app.run(debug=True)