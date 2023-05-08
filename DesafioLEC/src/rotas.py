from app import *
from db import adicionar_contato, selecionar_usuarios, cadastro, login

admins=["admin"]
logina = False

@app.route("/")
def index():
    return redirect("/home")

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

@app.route("/users")
def users():
    if logina and username in admins:
        userDetails = selecionar_usuarios()
        return render_template("users.html", userDetails=userDetails)
    else:
        return "Você não pode acessar essa página logue com um usuário administrador."

@app.route("/login", methods=["GET", "POST"])
def loginroute():
    global logina
    global username
    if request.method == "POST":
        username = request.form["username"]
        passwd = request.form["passwd"]
        logina, username = login(username=username, passwd=passwd)
        if logina:
            return redirect('/user')
        else:
            return "Login não realizado!"
    return render_template("lec.html", lec="login", login=True)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastroroute():
    if request.method == "POST":
        username = request.form["username"]
        passwd = request.form["passwd"]
        cadastroa = cadastro(username=username, passwd=passwd)
        if cadastroa:
            return redirect('/user')
        else:
            return "Cadastro não realizado!"
    return render_template("lec.html", lec="cadastro", login=False)

@app.route('/user', methods=["GET", "POST"])
def user():
    global logina
    global username
    if request.method == "GET":
        if logina:
            return render_template("user.html", username=username, admins=admins)
        else:
            return redirect("/login")
    else:
        sair = request.form['sair']
        if sair:
            logina = False
            username = ""
            return redirect('/home')