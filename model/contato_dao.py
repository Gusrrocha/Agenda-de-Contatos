import sqlite3
from model import dbase
from model.contatos import Contatos
lista = []
def insert(contato): # insere
    lista.append(contato)
    try:
        conn = dbase.connect() # conecta
        cursor = conn.cursor() # se move no banco
        sql = """INSERT INTO Contato (nome, sobrenome, empresa, cargo, email, telefone, obs, favorito)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(sql, contato.getContato())
        conn.commit()

    except Exception as e:
        print("Deu erro!!")
        print(e)
    finally:
        conn.close()

def update(contato): # atualiza
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """UPDATE Contato SET nome=?, sobrenome=?, empresa=?, cargo=?, email=?, telefone=?, obs=?, favorito=?; WHERE id=?"""
        l = contato.getContato()
        # insere o id no final da lista para ficar igual a sequência do sql
        l.append(contato.id)
        cursor.execute(sql, l)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def update_favorito(id, favorito):
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """UPDATE Contato SET favorito=? WHERE id=?"""
        cursor.execute(sql, [favorito, id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
def update_lixeira(id, deletado):
    try:
        conn = dbase.connect
        cursor = conn.cursor()
        sql = """UPDATE Contato SET deletado=? WHERE id=?"""
        cursor.execute(sql, [deletado, id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
def delete(id): # deleta
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Contato WHERE id = ?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def selectAll(): # pega todos
    lista = []
    try:
        conn = dbase.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Contato WHERE deletado = 0 ORDER BY upper(nome)"""
        cursor.execute(sql)
        result = cursor.fetchall() # retorna uma lista com os dados de cada contato
        for r in result:
            novo_contato = Contatos(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9])
            lista.append(novo_contato)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista