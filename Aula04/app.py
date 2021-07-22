from flask import Flask,render_template , request, redirect

app = Flask(__name__)
itens = []


@app.route('/')

def index():
    return render_template("index.html", titulo='TO DO LIST', itens = itens)

@app.route('/new', methods =['POST','GET'])

def new():
    if request.method == "POST":
        item = request.form['item']

    itens.append(item)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True) 