from flask import Flask
from flask_cors import CORS


DEV_FRONTEND = "http://localhost:3000"
# PROD_FRONTEND = ""


app = Flask(__name__)
CORS(app, origins=[
    DEV_FRONTEND, 
    # PROD_FRONTEND
])

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pet")
def get_pet():
    return "Teddy"
