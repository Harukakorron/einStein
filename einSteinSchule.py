from flask import Flask
from flask import render_template
from flask import request
import user
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
                      <div><label>Firstname: <input type="text" name="first_name"></label></div>
                      <div><label>Lastname: <input type="text" name="last_name"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
     else:
        username = request.form.get("username")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        user = user.User(username, firstname, lastname)
        user.to_db()
        return f"USer {username} was created"