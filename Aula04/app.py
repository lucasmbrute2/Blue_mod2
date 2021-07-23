from flask import Flask, render_template , request , redirect

app = Flask(__name__)
itens = []

#Para acessar o back-end são necesessárias as rotas para estabelecerem as conexões, como abaixo, na "route". O caminho "/" é padrão, a tela inicial do site.
@app.route("/") #toda rota deve obrigatoriamente começar com "/"
def index():  #Aqui é uma função normal.
    return render_template("index.html", titulo = "Nice title Bro", itens= itens) #render_template renderiza uma página.


@app.route("/new", methods=["POST","GET"])
def new_title():
    if request.method == 'POST':
        item = request.form['item']
        itens.append(item)
        return redirect('/')


@app.route('/clear')
def limpar():
    itens.clear()
    return redirect('/')
















# @app.route('/contato')   Testando abrir outra página
# def index2():
#     return render_template('index2.html')
if __name__ == '__main__':
    app.run(debug=True)

