from app import *
from db import adicionar_contato

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')


@app.route('/contato', methods=["POST", "GET"])
def contato():
    if request.method == "POST":
        email = request.form["semail"]
        assunto = request.form["assunto"]
        descricao = request.form["descricao"]

        adicionar_contato(email=email, assunto=assunto, descricao=descricao)

        return "Sucesso"
    return render_template('contato.html')