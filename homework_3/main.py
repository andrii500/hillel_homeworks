from flask import Flask, render_template
from faker import Faker
import csv
import requests


app = Flask(__name__)
fake = Faker()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/requirements")
def get_requirements():
    with open("requirements.txt") as f:
        data = ""
        for line in f:
            data += f"<p>{line}</p>"
        return data


@app.route("/generate-users/<num>")
def get_users(num):
    data = ''
    for _ in range(int(num)):
        data += f"<p>{fake.name()} - {fake.email()}</p>"
    return data


@app.route("/mean")
def get_mean():
    with open("hw.csv", encoding="utf-8") as f:
        file = csv.DictReader(f, delimiter=",")
        count = 0
        height = 0
        weight = 0
        for row in file:
            height += float(row[' "Height(Inches)"'])
            weight += float(row[' "Weight(Pounds)"'])
            count += 1
        return f""" <p>Average height {height / count} Inches</p>
                    <p>Average weight {weight / count} Pounds</p>"""


@app.route("/space")
def get_number_of_astros():
    r = requests.get('http://api.open-notify.org/astros.json')
    return f"<p>The number of astronauts at the moment - {r.json()['number']}</p>"
