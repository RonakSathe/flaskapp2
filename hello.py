from flask import Flask, render_template



#Create a Flask Instance
app = Flask(__name__)


#create a route decorator
@app.route('/')

#def index():
#    return "<h1>Hello World!</h1>"
def index():
    first_name = "john"
    stuff = "This is bold Text"
    favourite_pizza = ["Pepperoni","onion","Tomato"]
    return render_template("index.html",first_name = first_name,stuff=stuff,favourite_pizza=favourite_pizza)

#FILTERS>???
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags
#


#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

#Create custom error pages
#Ivalid URL
@app.errorhandler(404)
def page_no_found(e):
    return render_template("404.html"),404


#Internal Server ERROR Thang
@app.errorhandler(500)
def page_no_found(e):
    return render_template("500.html"),500

