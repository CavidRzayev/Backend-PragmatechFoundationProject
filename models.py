from app import db
from datetime import datetime,date



class Home(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    text=db.Column(db.String(50),nullable=False)



# class About(db.Model):
#     about_id=db.Column(db.Integer,primary_key=True)
#     about_text=db.Column(db.String(255),nullable=False)
#     about_title=db.Column(db.String(50),nullable=False)
#     skills=db.relationship("Skill",backref='about',lazy=True)


# class Skill(db.Model):
#     skill_id=db.Column(db.Integer,primary_key=True)
#     percent=db.Column(db.Integer,nullable=False)
#     about_id=db.Column(db.Integer,db.ForeignKey("about.about_id"),nullable=False)


class Services(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    text=db.Column(db.String(50),nullable=False)



class Resume(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(255),nullable=False)
    fullname=db.Column(db.String(50),nullable=False)




class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(50),nullable=False)
    title=db.Column(db.String(50),nullable=False)




class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(55))
    surname=db.Column(db.String(55))
    subject=db.Column(db.String(155))
    message=db.Column(db.String(255))
   




class Footer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about=db.Column(db.String(55))
    connect=db.Column(db.String(55))
    navagation=db.Column(db.String(155))
    services=db.Column(db.String(255))
    contact=db.Column(db.String(255))
   
