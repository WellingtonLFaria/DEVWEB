from app import *

app.config["MYSQL_Host"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "fatec"
app.config["MYSQL_DB"] = "unes"

db = MySQL(app)

def adicionar_contato(email, assunto, descricao):
    """Adiciona um contato a base de dados
    """
    cursor = db.connection.cursor()
    cursor.execute(f"INSERT INTO contatos(email, assunto, descricao) VALUES ('{email}', '{assunto}', '{descricao}')")

    db.connection.commit()

    cursor.close()

def selecionar_usuarios():
    cursor = db.connection.cursor()
    users = cursor.execute("SELECT * FROM contatos")
    if users > 0:
        userDetails = cursor.fetchall()
        return userDetails