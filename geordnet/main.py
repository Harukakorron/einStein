from flask import Flask
from flask import render_template
from flask import request
import sqlite3
import users
import minecraft
import stones
import Deutschland
import orte

app = Flask(__name__)


@app.route("/hello/<string:username>")
def hello_user(username):
    user = users.from_db(username)
    return f"<html><head></head><body>Hello <b>{user.username} </b></body></html>"

##@app.route("/hello_flask")
##def hello_flask():
##    return render_template(
##        "template.html",
##        title="Hello Flask",
##        description="This is my last one!")
##
##@app.route("/hello_flask2")
##def hello_flask2():
##    return render_template(
##        "template.html",
##        title="Hello Flask2",
##        description="This is my second-last one!")

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
        User = users.User(username, firstname, lastname)
        User.to_db()
        return f" Der Benutzer {username} wurde erstellt"

#@app.route("/search", mehtods =["GET", "POST"])
#def search_form():
#    if request.method == "GET":
#        return'''
#                <form method ="POST">
#                   <div><label>Suche: <input type ="text" name="SUCHE"></label></div>
#                </form>'''
#    else:
#        suche.from_db()
    
@app.route("/add_stones", methods=["GET", "POST"])
def stone_form():
     if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Name: <input type="text" name="Name"></label></div>
                      <div><label>Formeleinheit: <input type="text" name="Formeleinheit"></label></div>
                      <div><label>Verwendung: <input type="text" name="Verwendung"></label></div>
                      <div><label>Härte: <input type="REAL" name="Härte"></label></div>
                      <div><label>Farbe: <input type="text" name="Farbe"></label></div>
                      <div><label>Zugehörigkeit: <input type="text" name="Zugehörigkeit"></label></div>
                      <div><label>Gefahr: <input type="text" name="Gefahr"></label></div>
                      <div><label>Nummer: <input type="INTEGER" name="Nummer"></label></div>
                      <div><label>Oberklasse: <input type="text" name="Oberklasse"></label></div>
                      <div><label>Bild: <input type="BLOB" name="Bild"></label></div>
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
        stone = stones.stone(Name, Formeleinheit, Verwendung, Härte, Farbe, Zugehörigkeit, Gefahr, Nummer, Oberklasse, Bild)
        stone.to_db()
        return f" Der Stein {Name} wurde erstellt"

@app.route("/add_minecraft", methods=["GET", "POST"])
def minecraft_form():
     if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Name: <input type="text" name="Name"></label></div>
                      <div><label>Dimension: <input type="text" name="Dimension"></label></div>
                      <div><label>Höhe_mit_höchster_Wahrscheinlichkeit: <input type="INTEGER" name="Höhe mit höchster Wahrscheinlichkeit"></label></div>
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
        Mine.to_db()
        return f"{Name} wurde erstellt"  

@app.route("/add_land", methods=["GET", "POST"])
def doitsu_form():
     if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Nummer: <input type="INTEGER" name="Nummer"></label></div>
                      <div><label>Land: <input type="text" name="Land"></label></div>
                      <div><label>Bundesland: <input type="text" name="Bundesland"></label></div>
                      <div><label>Stein: <input type="text" name="Stein"></label></div>
                      <div><label>Abbaumethode: <input type="text" name="Abbaumethode"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
     else:
        Nummer = request.form.get("Nummer")
        Land = request.form.get("Land")
        Bundesland = request.form.get("Bundesland")
        Stein = request.form.get("Stein")
        Abbaumethode = request.form.get("Abbaumethode")
        doitsu = Deutschland.doitsu(Nummer, Land, Bundesland, Stein, Abbaumethode)
        doitsu.to_db()
        return f" Das Land {Land} wurde erstellt"
    
@app.route("/add_oertchen", methods=["GET", "POST"])
def ortle_form():
     if request.method == "GET":
        return '''
                  <form method="POST">
                      <div><label>Nummer: <input type="text" name="INTEGER"></label></div>
                      <div><label>Land: <input type="text" name="Land"></label></div>
                      <div><label>Stein: <input type="text" name="Stein"></label></div>
                      <div><label>Abbaumethode: <input type="text" name="Abbaumethode"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
     else:
        Nummer = request.form.get("Nummer")
        Land = request.form.get("Land")
        Stein = request.form.get("Stein")
        Abbaumethode = request.form.get("Abbaumethode")
        ortle = orte.ortle(Nummer, Land, Stein, Abbaumethode)
        ortle.to_db()
        return f" Das Land {Land} wurde erstellt"

@app.route('/')
def home():
   return render_template('einstein.html')

@app.route('/steinetabelle')
def steinetabelle():
    mycursor = app.dbcursor
    headings= ("Name", "Farbe", "Oberklasse", "Zugehörigkeit", "Verwendung", "Gefahr", "Härte", "Formeleinheit", "Bild")
    stonedata = mycursor.execute("Select Name, Farbe, Oberklasse, Zugehörigkeit, Verwendung, Gefahr, Härte, Formeleinheit, Bild from Steine;")
    stonedata = tuple(map(lambda x: ((x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]), x[8], x[0]), stonedata))
##    stonedata = tuple(filter(lambda x: x[0].find(mytext) >= 0))
    searchString = str(request.args.get('searchString'))
    if searchString != 'None' and len(searchString.strip()) > 0:
        stonedata = filter(lambda x: (x[0][0] != None and x[0][0].find(searchString) >= 0) or \
                           (x[0][1] != None and x[0][1].find(searchString) >= 0) or \
                           (x[0][2] != None and x[0][2].find(searchString) >= 0) or \
                           (x[0][3] != None and x[0][3].find(searchString) >= 0) or \
                           (x[0][4] != None and x[0][4].find(searchString) >= 0) or \
                           (x[0][5] != None and x[0][5].find(searchString) >= 0) or \
                           (x[0][7] != None and x[0][7].find(searchString) >= 0),
                                 stonedata)
    else:
        searchString = '*'
    stonedata = tuple(stonedata)
    return render_template('steinetabelle.html',
                           headings=headings,
                           stonedata=stonedata,
                           searchString=searchString,
                           foundsets=len(stonedata))
##    x[0].find(mytext) >= 0

@app.route('/ortetabelle')
def ortetabelle():
    mycursor = app.dbcursor
    headings= ("Land", "Stein", "Abbaumethode")
    stonedata = tuple(mycursor.execute("Select Land, Stein, Abbaumethode from Orte;"))
##    stonedata = tuple(map(lambda x: x[0], x[1], x[2] stonedata)
##    stonedata = tuple(filter(lambda x: x.find(mytext) >= 0))
    searchString = str(request.args.get('searchString'))
    if searchString != 'None' and len(searchString.strip()) > 0:
        stonedata = filter(lambda x: (x[0] != None and x[0].find(searchString) >= 0) or \
                           (x[1] != None and x[1].find(searchString) >= 0) or \
                           (x[2] != None and x[2].find(searchString) >= 0),
                                 stonedata)
    else:
        searchString = '*'
    stonedata = tuple(stonedata)
    return render_template('ortetabelle.html',
                           headings=headings,
                           stonedata=stonedata,
                           searchString=searchString,
                           foundsets=len(stonedata))

@app.route('/deutschlandtabelle')
def deutschlandtabelle():
    mycursor = app.dbcursor
    headings= ("Land", "Bundesland", "Stein", "Abbaumethode")
    stonedata = list(mycursor.execute("Select Land, Bundesland, Stein, Abbaumethode from Deutschland;"))
    searchString = str(request.args.get('searchString'))
    if searchString != 'None' and len(searchString.strip()) > 0:
        stonedata = filter(lambda x: (x[0] != None and x[0].find(searchString) >= 0) or \
                           (x[1] != None and x[1].find(searchString) >= 0) or \
                           (x[2] != None and x[2].find(searchString) >= 0) or \
                           (x[3] != None and x[3].find(searchString) >= 0),
                                 stonedata)
    else:
        searchString = '*'
    stonedata = tuple(stonedata)
    return render_template('deutschlandtabelle.html',
                           headings=headings,
                           stonedata=stonedata,
                           searchString=searchString,
                           foundsets=len(stonedata))
        
@app.route('/minetab')
def minetab():
    mycursor = app.dbcursor
    stonedata = mycursor.execute("Select * from Minecraft;")
    stonedata = tuple(map(lambda x: ((x[0],x[1],x[2],x[3],x[4],x[5]), x[6], x[0]), stonedata))

    headings= ("Name", "Dimension", "Höhe_mit_höchster_Wahrscheinlichkeit", "Biom", "Farbe", "real_life", "Bild")

    searchString = str(request.args.get('searchString'))
    if searchString != 'None' and len(searchString.strip()) > 0:
        stonedata = filter(lambda x: (x[0][0] != None and x[0][0].find(searchString) >= 0) or \
                           (x[0][1] != None and x[0][1].find(searchString) >= 0) or \
                           (x[0][2] != None and x[0][2].find(searchString) >= 0) or \
                           (x[0][3] != None and x[0][3].find(searchString) >= 0) or \
                           (x[0][4] != None and x[0][4].find(searchString) >= 0) or \
                           (x[0][5] != None and x[0][5].find(searchString) >= 0),
                                 stonedata)
    else:
        searchString = '*'
    stonedata = tuple(stonedata)

    return render_template('minetab.html',
                           headings=headings,
                           stonedata=stonedata,
                           searchString=searchString,
                           foundsets=len(stonedata))

@app.route('/einStein')
def einStein():
    return render_template('einstein.html')

##@app.route('/table')
##def table():
##    mycursor = app.dbcursor
####    stonedata = mycursor.execute("Select * from Minecraft;")
####    headings= ("Name", "Dimension", "Höhe_mit_höchster_Wahrscheinlichkeit", "Biom", "Farbe", "real_life", "Bild")
##    headings = ('a', 'b','c')
##    stonedata = (('1', '1', '1'),
##                ('ujg', 'g', 'zugf'),
##                ('UZGT', 'zf', 'g'),
##                )
##    
##    return render_template('table.html',
##                            headings=headings,
##                            stonedata=stonedata)
##


if __name__ == '__main__':
    app.debug = False
    
    app.dbconnection = sqlite3.connect("ding_bis_jetzt.db",  check_same_thread=False) # Muss vorher angelegt werden.
    app.dbcursor = app.dbconnection.cursor()

    app.run()
