#coding: UTF-8
from flask import Flask, render_template, request

app =  Flask(__name__)

@app.route("/")
def pagina_index():
    return render_template("index.html")
	
	
@app.route("/dados_pessoais/")
def dadosget():
    nome = request.args.get("nome")
    mail = request.args.get("e-mail")
    tel = request.args.get("telefone")
    return render_template("dados.html", **locals() )
	
	
@app.route("/dados_pessoais/", methods=["POST"])
def dadospost():
    nome = request.form.get("nome")
    mail = request.form.get("e-mail")
    tel = request.form.get("telefone")
    return render_template("dados.html", **locals() )

@app.route("/dados_pessoais/<nome>/<mail>/<tel>")
def metodo3(nome, mail, tel):
    return render_template("dados.html", **locals() )
	