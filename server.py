from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def paginaInicial():
    """
    hobbies = ["Futbol", "Programar", "Peliculas"]
    return render_template("index.html", nombre="Victor", apellido="Vasquez", hobbies=hobbies )
    """
    return "Hola Mundo"

@app.route('/play/<int:num>', methods=['GET'])
def jugar(num):
    return render_template("index.html", num=num)

@app.route('/play/<int:num>/<string:color>', methods=['GET'])
def jugarColor(num, color):
    return render_template("index.html", num=num, color=color)

if __name__ == "__main__":
    app.run(debug = True)
