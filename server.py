from flask import Flask, render_template, g
import sqlite3
import Base
import forms

app = Flask(__name__)
app.config['DATABASE'] = "static/db/voyage.db"
app.secret_key = "qwert1234"

def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    return con

def get_connect():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

navMenu = [
    {"link": "/index/", "name": "Главная"},
    {"link": "/voyages/", "name": "Путешествия"},
    {"link": "/add/", "name": "Добавить"},
    {"link": "/info/", "name": "О нас"}
]

@app.route("/index/")
@app.route("/")
def index():
    return render_template("index.html", menu=navMenu)

@app.route("/info/")
def info():
    return render_template("info.html", menu=navMenu)

@app.route("/voyages/")
def voyages():
      
    baseObject = Base.VoyageDB(get_connect())
    lst = baseObject.getAllVoyages()
    return render_template("voyages.html", menu=navMenu, cardsList=lst)

@app.route("/add/", methods=["POST", "GET"])
def add():
    addForm = forms.AddType()
    con = get_connect()
    bd = Base.VoyageDB(con)
    if addForm.name.data:
        bd.addType(
            addForm.name.data,
            addForm.description.data                  
        )
    return render_template("add.html", menu=navMenu, form=addForm)


if __name__ == "__main__":
    app.run()
    