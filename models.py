from app import db
from datetime import datetime,date

# --------------------------------------------Home-------------------------


class Home(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    text=db.Column(db.String(50),nullable=False)
    image = db.Column(db.String,nullable=False)



# -------------------------------------------About---------------------------

class Skill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    percent=db.Column(db.Integer,nullable=False)
    name=db.Column(db.String(50),nullable=False)
    abouts = db.relationship('About',backref='skill',lazy=True)



class About(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(255))
    title=db.Column(db.String(50))
    image=db.Column(db.String)
    skill_id = db.Column(db.Integer,db.ForeignKey('skill.id'),nullable=False)


# ------------------------------------------Portfolio---------------------------

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String,nullable=False)
    portfolies = db.relationship('Portfolio',backref='category',lazy=True)

class Portfolio(db.Model):
    portfolio_id = db.Column(db.Integer, primary_key=True)
    portfolio_title = db.Column(db.String,nullable=False)
    portfolio_image = db.Column(db.String,nullable=False)
    category_id=db.Column(db.Integer, db.ForeignKey('category.category_id'),nullable=False)




# ---------------------------------------------Services-------------------------



class Services(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    text=db.Column(db.String(50),nullable=False)

# ----------------------------------------------Resume-------------------------


class Resume(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(255),nullable=False)
    fullname=db.Column(db.String(50),nullable=False)
    image=db.Column(db.String)

# -----------------------------------------------Blog-------------------------



class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(50),nullable=False)
    title=db.Column(db.String(50))
    image=db.Column(db.String)
    time=db.Column(db.DateTime)

# -----------------------------------------------Contact-------------------------


class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(55))
    surname=db.Column(db.String(55))
    subject=db.Column(db.String(155))
    message=db.Column(db.String(255))

   
# -----------------------------------------------Footer-------------------------




class Footer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about=db.Column(db.String(55))
    navagation=db.Column(db.String(155))
    services=db.Column(db.String(255))
    contact=db.Column(db.String(255))
    elaqe=db.Column(db.String(255))
    text=db.Column(db.String(255))
    name=db.Column(db.String(255))
    name1=db.Column(db.String(255))
    title=db.Column(db.String(255))
    adress=db.Column(db.String(255))
    email=db.Column(db.String(255))



   



#------Network--------

class Connect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    instagram = db.Column(db.String)
    pinterest = db.Column(db.String)
    twitter = db.Column(db.String)
    facebook = db.Column(db.String)
    linkedin = db.Column(db.String)
    dribble = db.Column(db.String)






















