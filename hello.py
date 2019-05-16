from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/<name>")
def hello_someone(name):
            return render_template("hello.html", name=name.title())
            
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    email = form_data["email"]
    print(email)
    return "All OK, "+email

app.run(debug=False)
