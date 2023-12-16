from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    gender = db.Column(db.String(10))

    def __init__(self,name,age,email,gender):
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender
    
    def as_dict(self):
        return {c.name: str(getattr(self,c.name)) for c in self.__table__.columns}