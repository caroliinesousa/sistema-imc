
import sqlite3

def criar_tabela_clientes():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    altura REAL NOT NULL,
    peso REAL NOT NULL)
    """)
    conexao.commit()

def adicionar_clientes(clientes):
    cursor.executemany('''
    INSERT INTO clientes (nome, idade, altura, peso)
    VALUES (?, ?, ?, ?)
    ''', clientes)
    conexao.commit()

def adicionar_cliente(nome_cliente, idade_cliente, altura_cliente, peso_cliente):
    """
    Funcao que adiciona um cliente na base de dados.
    :param nome_cliente: nome
    :param idade_cliente: idade
    :param altura_cliente: altura
    :param peso_cliente: peso
    :return: None
    """
    cursor.execute('''
    INSERT INTO clientes(nome, idade, altura, peso)
    VALUES(?, ?, ?, ?)
    ''', (nome_cliente, idade_cliente, altura_cliente, peso_cliente))
    conexao.commit()

def consultar_imc(nome_cliente):
    cursor.execute('''
    SELECT nome, altura, peso 
    FROM clientes
    where nome = ?
    ''', (nome_cliente,))
    cliente = cursor.fetchone()

    if cliente:
        nome, altura, peso = cliente
        imc = peso / (altura ** 2)
        return f"0 usuario {nome} tem IMC = {imc:.2f}"
    else:
        return "cliente não encontrado! adicione o cliente no sistema!"

def usuario_consulta_imc():
    print('\nInforme o nome do cliente para calcular o seu IMC: ')
    nome_pesquisa = input("Nome:")
    print(consultar_imc(nome_pesquisa))

def usuario_adiciona_cliente():
    print('\nInforme abaixo os dados do cliente para cadastro: ')
    nome = input('Nome: ')
    idade = input('Idade: ')
    altura = input('Altura: ')
    peso = input('Peso: ')
    adicionar_cliente(nome, idade, altura, peso)
    print('Cliente cadastrado com sucesso!')

def consultar_cadastro(nome_para_consultar):
    cursor.execute('''
        SELECT nome 
        FROM clientes
        where nome = ?
        ''', (nome_para_consultar,))
    cliente = cursor.fetchone()
    if cliente:
        return 'Cliente encontrado!'
    else:
        return 'Cliente não encontrado! cadastre o cliente no sistema.'

def usuario_consulta_cadastro():
    print('Bem vindo de volta! Informe o nome do cliente a ser pesquisado no sistema. ')
    nome_consulta = input('Nome: ')
    print(consultar_cadastro(nome_consulta))
    return nome_consulta

def aplicacao():
    nome_cliente = usuario_consulta_cadastro()
    if 'Cliente encontrado!' != consultar_cadastro(nome_cliente):
        usuario_adiciona_cliente()
        print(consultar_imc(nome_cliente))
    else:
        print(consultar_imc(nome_cliente))

if __name__ == '__main__':
    conexao = sqlite3.connect('clinica.db')
    cursor = conexao.cursor()
#sistema
    criar_tabela_clientes()

    clientes = [
        ('Ana', 26, 1.60, 60),
        ('Carol', 25, 1.67, 65),
        ('Vitor', 26, 1.60, 58),
        ('Rita', 65, 1.50, 55),
        ('Bruno', 28, 1.70, 70),
        ('Joana', 22, 1.65, 27),
    ]
    adicionar_clientes(clientes)
#usuario
    aplicacao()