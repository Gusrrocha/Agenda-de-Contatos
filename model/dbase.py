import sqlite3

# conexão do banco de dados
def connect():
    # cria a conexão
    conn = sqlite3.connect('database/contatos.sqlite')
    return conn