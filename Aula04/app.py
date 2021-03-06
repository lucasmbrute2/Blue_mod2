from flask import Flask, render_template , request , redirect

app = Flask(__name__)
itens = []

#Para acessar o back-end são necesessárias as rotas para estabelecerem as conexões, como abaixo, na "route". O caminho "/" é padrão, a tela inicial do site.
@app.route("/") #toda rota deve obrigatoriamente começar com "/"
def index():  #Aqui é uma função normal.
    return render_template("index.html", titulo = "TO DO LIST", itens= itens) #render_template renderiza uma página.


@app.route("/new", methods=["POST","GET"])
def new():
    if request.method == 'POST':
        item = request.form['item'] #é criada uma variável para receber oq o input está mandando, no caso o name é 'item' por isso fica dessa forma: request.form['item'].
        itens.append(item)
        return redirect('/')


@app.route('/clear')
def limpar():
    itens.clear()
    return redirect('/')



@app.route('/newPage') #criei uma nova página
def nova_pagina():
    return render_template('index2.html', itens = itens )


@app.route('/voltar')
def volta_pagina():
    return redirect('/')


@app.route('/newButton', methods = ['POST', 'GET']) #Aqui eu criei um botão para mudar de página mantendo a lista (apenas como teste)
def novo_item():
    item = request.form['item']
    itens.append(item)
    return redirect('/newPage')





if __name__ == '__main__':
    app.run(debug=True)

