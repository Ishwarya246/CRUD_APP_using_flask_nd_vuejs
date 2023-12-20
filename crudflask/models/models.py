from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer , primary_key=True)
    rollno = db.Column(db.Integer )
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    

    def __init__(self,rollno,name,age,email):
        self.name = name
        self.age = age
        self.email = email
        self.rollno = rollno
    
    def as_dict(self):
        return {c.name: str(getattr(self,c.name)) for c in self.__table__.columns}