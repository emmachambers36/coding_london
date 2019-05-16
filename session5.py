from flask import Flask, render_template, request
import requests

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
    subject = "How are you doing?"
    send_simple_message(email, subject)
    print(email)
    return "All OK, "+email

@app.route("/weather", methods=["POST"])
def weatherIn():
    form_data = request.form
    city = form_data["city"]
    weather(city)
    print(city)
    return "All OK, "+city


def send_simple_message(email, subject):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc748cb30c0cd4046b27a04f609de7430.mailgun.org/messages",
        auth=("api", "ac0891cd26b595ea64a3db7783428955-e566273b-5e1af0b6"),
        data={"from": "Excited User <mailgun@sandboxc748cb30c0cd4046b27a04f609de7430.mailgun.org>",
              "to": [email],
              "subject": subject,
              "text": "Testing some Mailgun awesomness!"})

def weather(city):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    payload = {"q": "London,UK", "units":"metric", "appid":"6c4209ee7962cb590f73efe93e96e8dd"}

    response = requests.get(endpoint, params=payload)

    import requests
endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"YOUR_APP_ID"}
response = requests.get(endpoint, params=payload)
data = response.json()
print data'main'
print response.url
print response.status_code
print response.headers["content-type"]
print response.text

temperature = data["main"]["temp"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"It's {}C in {}, and the sky is {}".format(temperature, name, weather)


app.run(debug=False)
