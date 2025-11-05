from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

def ConectarBanco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="fastphone",
    )

app = Flask(__name__)

# -------------------------
# Página inicial
# -------------------------
@app.route('/')
def index():
    return render_template('index.html')

# -------------------------
# Cadastrar vendedores
# -------------------------
@app.route('/cadastrar_vendedores', methods=['GET', 'POST'])
def cadastrar_vendedores():
    if request.method == 'POST':
        nome = request.form['nome']

        try:
            conexao = ConectarBanco()
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO vendedores (nome) VALUES (%s)", (nome,))
            conexao.commit()
            cursor.close()
            conexao.close()
            return redirect(url_for('index'))
        except Error as e:
            return f"Erro ao cadastrar vendedor: {e}"

    return render_template('cadastrar_vendedores.html')

# -------------------------
# Cadastrar produtos
# -------------------------
@app.route('/cadastrar_produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']

        try:
            conexao = ConectarBanco()
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO produtos (nome, categoria) VALUES (%s, %s)", (nome, categoria))
            conexao.commit()
            cursor.close()
            conexao.close()
            return redirect(url_for('index'))
        except Error as e:
            return f"Erro ao cadastrar produto: {e}"

    return render_template('cadastrar_produto.html')

# -------------------------
# Cadastrar venda
# -------------------------
@app.route('/cadastrar_venda', methods=['GET', 'POST'])
def cadastrar_venda():
    conexao = ConectarBanco()
    cursor = conexao.cursor()

    # sempre busca as listas de produtos e vendedores para o formulário
    cursor.execute("SELECT id, nome FROM produtos ORDER BY nome")
    produtos = cursor.fetchall()

    cursor.execute("SELECT id, nome FROM vendedores ORDER BY nome")
    vendedores = cursor.fetchall()

    if request.method == 'POST':
        produto_id = request.form['produto_id']
        vendedor_id = request.form['vendedor_id']
        quantidade = request.form['quantidade']
        preco_unit = request.form['preco_unit']
        data_venda = request.form['data_venda']   # novo campo

        try:
            cursor.execute(
            "INSERT INTO vendas (produto_id, vendedor_id, quantidade, preco_unit, data_venda) VALUES (%s, %s, %s, %s, %s)",
            (produto_id, vendedor_id, quantidade, preco_unit, data_venda)
        )
            conexao.commit()
            return redirect(url_for('index'))
        except Error as e:
            return f"Erro ao registrar venda: {e}"
        finally:
            cursor.close()
            conexao.close()

    cursor.close()
    conexao.close()
    return render_template('cadastrar_venda.html', produtos=produtos, vendedores=vendedores)

# -------------------------
# Executar aplicação
# -------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5001)
