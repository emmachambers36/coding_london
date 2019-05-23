from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template("helloworld.html")

@app.route("/<name>")
def hi(name):
   return render_template("helloworld.html", userName=name)
