from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("profile.html")

@app.route("/myName/<my_name>")
def my_name(my_name):
    return "my name is {}".format(my_name)

if __name__ == '__main__':
    app.run()
