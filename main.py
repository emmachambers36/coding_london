from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<page1>")
def page1():
        return render_template("page1.html")
