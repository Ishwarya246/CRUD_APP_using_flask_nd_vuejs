from flask import Flask,jsonify,request
from models.models import db, Student 
from flask_cors import CORS
from uuid import uuid4
from sqlalchemy import asc

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:1234@localhost/Crudapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def home():
    print("Hello")
    return "Welcome To the CRUD Appliation"

@app.route('/select',methods=["GET"])
def select():
    record = Student.query.order_by(asc(Student.rollno)).all()
    response = []
    for i in record:
        d = i.as_dict()
        response.append(d)
    return jsonify(response)

@app.route("/insert" , methods=["POST"])
def insert():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")
    email = data.get("email")
    rollno = data.get("rollno")

    student = Student.query.filter_by(rollno = rollno).first()

    if not student :
        student = Student(
                          name = name,
                          age = age,
                          email = email,
                          rollno = rollno)
        db.session.add(student)
        db.session.commit()
        return jsonify({"message" : "Success" , "code" : 200 })
    
    else :
        return jsonify({"message" : "Student already exists" , "code" : 403})
    


@app.route("/delete" , methods= ["PUT"])
def delete():   

    data = request.get_json()
    rollno = data.get("rollno")
    student = Student.query.filter_by(rollno = rollno).first()

    if student:
        Student.query.filter_by(rollno = rollno).delete()
        db.session.commit()
        return jsonify({"message" : "Deleted Successfully" , "code" : 200})
    else :
        return jsonify({"message" : "Student does not exists" , "code" : 404})
    
    

@app.route("/update" , methods = ["PUT"])
def update():

    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    email = data.get("email")
    rollno = data.get("rollno")

    student = Student.query.filter_by(rollno = rollno).first()

    if student :

        setattr(student , "name" , name)
        setattr(student , "age" , age)
        setattr(student , "email" , email)
        setattr(student , "rollno" , rollno)

        db.session.commit()
        return jsonify({"message" : "Updated Successfully" , "code" : 200 })
    
    else :
        return jsonify({"message" : "Student doesnot exists" , "code" : 404})

app.run(debug=True)
