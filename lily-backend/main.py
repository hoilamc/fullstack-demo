from flask import Flask
from flask_cors import CORS


DEV_FRONTEND = "http://127.0.0.1:3000"

app = Flask(__name__)
CORS(app, origins=[
    DEV_FRONTEND, 
])

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pet")
def get_pet():
    return "Teddy"
