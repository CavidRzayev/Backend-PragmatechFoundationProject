from app import app,db
from forms import *
from models import *
from flask import render_template,redirect,request,url_for,Blueprint
import random
import os


blog = Blueprint(
    'blog',
    __name__,
    url_prefix='/blog',
    static_folder='static',
    template_folder='templates')


@app.route('/',methods=["GET","POST"])
def Index():
     ftr=Footer.query.all()
     con=Connect.query.all()
     skl=Skill.query.all()
     abt=About.query.all()
     categories=Category.query.all()
     portfolio=Portfolio.query.all()
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
     return render_template('app/index.html',srvc=srvc,blg=blg,rsm=rsm,Homm=Homm,categories=categories,portfolio=portfolio,skl=skl,abt=abt,con=con,ftr=ftr)


@app.route('/blog/<int:id>',methods=['GET','POST'])
def SingleBlog(id):
     ftr=Footer.query.all()
     Homm=Home.query.all()
     con=Connect.query.all()
     blog = Blog.query.get(id)
     return render_template('app/blog.html',blg=blog,con=con,ftr=ftr,Homm=Homm)