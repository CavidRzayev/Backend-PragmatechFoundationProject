from app import app,db
from forms import *
# from app.models import ContactForm
from models import *
from flask import render_template,redirect,request,url_for,Blueprint
import random
import os


@app.route('/',methods=["GET","POST"])
def Index():
     Homm=Home.query.all()
     rsm=Resume.query.all()
     blg=Blog.query.all()
     srvc=Services.query.all()
     if request.method == "POST":
          contact = Contact(
            name = request.form['fname'],
            surname = request.form['lname'],
            subject= request.form['text'],
            message= request.form['message']
          )
          db.session.add(contact)
          db.session.commit()
          return redirect ('/')
     return render_template('app/index.html',srvc=srvc,blg=blg,rsm=rsm,Homm=Homm)



@app.route('/blog/<int:id>',methods=['GET','POST'])
def SingleBlog(id):
    blog = Blog.query.get(id)
    return render_template('app/blog.html',blg=blog)