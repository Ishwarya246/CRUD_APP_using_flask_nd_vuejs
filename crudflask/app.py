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
    


@app.route("/delete" , methods= ["GET","DELETE"])
def delete():   

    data = request.get_json()
    email = data.get("email")

    student = Student.query.filter_by(email = email).first()

    if student:
        Student.query.filter_by(email = email).delete()
        db.session.commit()
        return jsonify({"message" : "Deleted Successfully" , "code" : 200})
    else :
        return jsonify({"message" : "Student does not exists" , "code" : 404})
    
    

@app.route("/update" , methods = ["PUT"])
def update():

    data = request.get_json()
    email = data.get("email")
    attribute = data.get("attribute")
    value = data.get("value")

    student = Student.query.filter_by(email = email).first()

    if student :

        setattr(student , attribute , value)
        db.session.commit()
        return jsonify({"message" : "Updated Successfully" , "code" : 200 })
    
    else :
        return jsonify({"message" : "Student doesnot exists" , "code" : 404})

app.run()
