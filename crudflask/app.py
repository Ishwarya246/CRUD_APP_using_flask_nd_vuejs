from flask import Flask,jsonify,request
from models.models import db, Student 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:1234@localhost/Crudapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def home():
    print("Hello")
    return "Welcome To the CRUD Appliation"

app.run()
