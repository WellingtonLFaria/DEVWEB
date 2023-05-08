from app import *

config = {
        'user': 'root',
        'password': 'Motoca007',
        'host': 'localhost',
        'port': '3306',
        'database': 'unes'
    }

db = mysql.connector.connect(**config)

def adicionar_contato(email, assunto, descricao):
    """Adiciona um contato a base de dados
    """
    cursor = db.cursor(buffered=True)
    cursor.execute(f"INSERT INTO contatos(email, assunto, descricao) VALUES ('{email}', '{assunto}', '{descricao}')")

    db.commit()

    cursor.close()

def selecionar_usuarios():
    cursor = db.cursor(buffered=True)
    users = cursor.execute("SELECT * FROM contatos")
    userDetails = cursor.fetchall()
    return userDetails

def cadastro(username, passwd):
    cursor = db.cursor(buffered=True)
    try:
        cursor.execute(f"INSERT INTO users(username, passwd) VALUES ('{username}', '{passwd}')")
        db.commit()
        cursor.close()
        return True
    except:
        return False

def login(username, passwd):
    login = False
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        if (username, passwd) == user:
            login = True
            break
    return login, username
