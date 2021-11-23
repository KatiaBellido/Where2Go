from flask import Flask, render_template, request, session, url_for

import os
import datetime
import pymongo
app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(days=360)
app.secret_key = os.environ.get('secret_key')

client = pymongo.MongoClient(
    "mongodb+srv://admin:Contras3na@where2go.hlnon.mongodb.net/test")

db = client.Where2Go
restaurantes = db.Restaurantes
museos = db.Museos
usuarios = db.Usuarios


@app.route('/')
def index():
    return render_template('/login.html')


@app.route('/login', methods=['POST'])
def login():
    # Permite obtener del form el nombre de las variables que necesitamos
    username = request.form["username"]
    password = request.form["password"]
    # Guarda los datos en la sesión
    # session["email"] = username
    # session["password"] = password
    try:
        filter = {"nombre": username}
        search = usuarios.find_one(filter)
        if search is not None:
            return render_template('/index.html')
        else:
            return "<p>el usuario con correo %s no existe<p>" % username
    except Exception as e:
        return "<p>Hay un error %s </p>" % e


@app.route('/signup', methods=["POST"])
def signup():
    name = request.form["username"]
    filter = {"nombre": request.form["username"]}
    search = usuarios.find_one(filter)
    if search is None:
        _user = {
            "nombre": request.form['username'],
            "mail": request.form['email'],
            "contrasena": request.form['password']
        }
        try:
            usuarios.insert_one(_user)
            return render_template('/index.html', message=name)
        except Exception as e:
            return "<p>Hay un error %s </p>" % e
    else:
        return "<p>el usuario %s ya existe<p>" % name

@app.route('/signup2') 
def signup2():
    return render_template('/signup.html')


@app.route('/categorias')
def categorias():
    return render_template('/categorias.html')

@app.route('/single')
def single():
    return render_template('/single.html')
