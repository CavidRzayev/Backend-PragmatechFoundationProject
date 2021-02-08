from app import app,db
from forms import *
from models import *
from flask import render_template,redirect,request,url_for,Blueprint
import random
import os


@app.route('/',methods=["GET","POST"])
def Index():
     ftr=Footer.query.all()
     con=Connect.query.all()
     skl=Skill.query.all()
     abt=About.query.all()
     ctg=Category.query.all()
     prt=Portfolio.query.all()
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
     return render_template('app/index.html',srvc=srvc,blg=blg,rsm=rsm,Homm=Homm,ctg=ctg,prt=prt,skl=skl,abt=abt,con=con,ftr=ftr)


@app.route('/blog/<int:id>',methods=['GET','POST'])
def SingleBlog(id):
    blog = Blog.query.get(id)
    return render_template('app/blog.html',blg=blog)