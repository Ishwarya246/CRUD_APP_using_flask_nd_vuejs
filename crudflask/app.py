from flask import Flask,jsonify,request
from models.models import db, Student 
from flask_cors import CORS
from uuid import uuid4

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:1234@localhost/Crudapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def home():
    print("Hello")
    return "Welcome To the CRUD Appliation"


@app.route("/insert" , methods=["POST"])
def insert():
    print("..........................")
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    email = data.get("email")
    gender = data.get("gender")

    student = Student.query.filter_by(email=email).first()
    # print(student)

    if not student :
        student = Student(
                          name = name,
                          age = age,
                          email = email,
                          gender = gender)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message" : "Success" , "code" : 200 })
    
    else :
        return jsonify({"message" : "Student already exists" , "code" : 403})

@app.route("/delete")
def delete():
    return 

@app.route("/edit")
def edit():
    return

app.run()
