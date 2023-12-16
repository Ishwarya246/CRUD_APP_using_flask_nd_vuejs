from flask import Flask,jsonify,request
from models.models import db, Student 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    print("Hello")
    return "Welcome To the CRUD Appliation"

app.run()
