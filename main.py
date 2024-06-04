from flask import Flask
from flask import render_template
from flask import request
import users
import minecraft
import stones
app = Flask(__name__)

@app.route("/") #oder dein dein eigener Pfad
def einStein():  # beliebiger Funktionsname
    return "einStein" # Der Text der unter der Route angezeigt wird.

@app.route("/hello/<string:username>")
def hello_user(username):
    user = users.from_db(username)
    return f"<html><head></head><body>Hello <b>{user.username} </b></body></html>"

@app.route("/hello_flask")
def hello_flask():
    return render_template(
        "template.html",
        title="Hello Flask",
        description="This is my last one!")

@app.route("/hello_flask2")
def hello_flask2():
    return render_template(
        "template.html",
        title="Hello Flask2",
        description="This is my second-last one!")

@app.route("/add_user", methods=["GET", "POST"])
def user_form():
     if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Username: <input type="text" name="username"></label></div>
                      <div><label>Firstname: <input type="text" name="firstname"></label></div>
                      <div><label>Lastname: <input type="text" name="lastname"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
     else:
        username = request.form.get("username")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        user = users.User(username, firstname, lastname)
        user.to_db()
        return f"User {username} was created"
    
@app.route("/add_stones", methods=["GET", "POST"])
def minecraft_form():
     if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Name: <input type="text" name="Name"></label></div>
                      <div><label>Formeleinheit: <input type="text" name="Formeleinheit"></label></div>
                      <div><label>Verwendung: <input type="text" name="Verwendung"></label></div>
                      <div><label>Härte: <input type="text" name="Härte"></label></div>
                      <div><label>Farbe: <input type="text" name="Farbe"></label></div>
                      <div><label>Zugehörigkeit: <input type="text" name="Zugehörigkeit"></label></div>
                      <div><label>Gefahr: <input type="text" name="Gefahr"></label></div>
                      <div><label>Nummer: <input type="text" name="Nummer"></label></div>
                      <div><label>Oberklasse: <input type="text" name="Oberklasse"></label></div>
                      <div><label>Bild: <input type="text" name="Bild"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
     else:
        Name = request.form.get("Name")
        Formeleinheit = request.form.get("Formeleinheit")
        Verwendung = request.form.get("Verwendung")
        Härte = request.form.get("Härte")
        Farbe = request.form.get("Farbe")
        Zugehörigkeit = request.form.get("Zugehörigkeit")
        Gefahr = request.form.get("Gefahr")
        Nummer = request.form.get("Nummer")
        Oberklasse = request.form.get("Oberklasse")
        Bild = request.form.get("Bild")
        Mine = minecraft.Mine(Name, Formeleinheit, Verwendung, Härte, Farbe, Zugehörigkeit, Gefahr, Nummer, Oberklasse, Bild)
        Mine.to_db()
        return f" stone {Name} was created"

@app.route("/add_minecraft", methods=["GET", "POST"])
def minecraft_form():
     if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Name: <input type="text" name="Name"></label></div>
                      <div><label>Dimension: <input type="text" name="Dimension"></label></div>
                      <div><label>Höhe_mit_höchster_Wahrscheinlichkeit: <input type="text" name="Höhe mit höchster Wahrscheinlichkeit"></label></div>
                      <div><label>Biom: <input type="text" name="Biom"></label></div>
                      <div><label>Farbe: <input type="text" name="Farbe"></label></div>
                      <div><label>real_life: <input type="text" name="real life"></label></div>
                      <div><label>Bild: <input type="text" name="Bild"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
     else:
        Name = request.form.get("Name")
        Dimension = request.form.get("Dimension")
        Höhe_mit_höchster_Wahrscheinlichkeit = request.form.get("Höhe mit höchster Wahrscheinlichkeit")
        Biom = request.form.get("Biom")
        Farbe = request.form.get("Farbe")
        real_life = request.form.get("real life")
        Bild = request.form.get("Bild")
        Mine = minecraft.Mine(Name, Dimension, Höhe_mit_höchster_Wahrscheinlichkeit, Biom, Farbe, real_life, Bild)
        mine.to_db()
        return f" minecraft {Name} was created"  
