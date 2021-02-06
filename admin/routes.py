from flask import Blueprint,render_template,redirect,request
from app import *
from . forms import BlogForm
import os
import random
from datetime import date
from app import db
# from app.models import ContactForm

admin = Blueprint('admin',__name__,url_prefix='/admin',static_folder='static',template_folder='templates')


@admin.route('/')
def adminindex():
    return render_template('admin/Contact/contact.html')

# ---------------------------------------------------CONTACT----------------------------------

@admin.route('/contact')
def contact():
    contacts = Contact.query.all()
    return render_template('admin/Contact/contact.html',cnc=contacts)
    
@admin.route('/contact/<int:id>')
def deleteContact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect ('/admin/contact')


# -----------------------------------------------------HOME---------------------------------------------------------------------------

@admin.route('/home' , methods=["GET","POST"])
def homepage():
    Homm=Home.query.all()
    if request.method == "POST":
        Homm=Home(title=request.form["title"], text=request.form["text"])
        db.session.add(Homm)
        db.session.commit()
        return redirect('/admin/home')
    return render_template('/admin/Home/home.html',Homm=Homm)

@admin.route('/home/<int:id>')
def deleteHome(id):
    Homm = Home.query.get(id)
    db.session.delete(Homm)
    db.session.commit()
    return redirect ('/admin/home')


# ----------------------------------------------------SERVICES---------------------------------------------------------------

@admin.route('/services' , methods=["POST" , "GET"])
def services(): 
    srvc=Services.query.all()
    if request.method == "POST":
        srvc=Services(title=request.form["title"], text=request.form["text"],)
        db.session.add(srvc)
        db.session.commit()
        return redirect ('/admin/services')
    return render_template('admin/Services/services.html',srvc=srvc)

@admin.route('/services/<int:id>')
def deleteServices(id):
    srvc = Services.query.get(id)
    db.session.delete(srvc)
    db.session.commit()
    return redirect ('/admin/services')
    





# ------------------------------------------------------BLOG---------------------------------------------------------------

@admin.route('/blog' , methods=["POST","GET"])
def blog():
    blg=Blog.query.all()
    if request.method == "POST":
        blg=Blog(text=request.form['text'],title=request.form['title'])
        # date=datetime.today()
        db.session.add(blg)
        db.session.commit()
        return redirect ('/admin/blog')
    return render_template('admin/Blog/blog.html',blg=blg)


@admin.route('/blog/<int:id>')
def deleteBlog(id):
    blg = Blog.query.get(id)
    db.session.delete(blg)
    db.session.commit()
    return redirect ('/admin/blog')

    
# @admin.route('/blog/<int:id>')
# def updateBlog(id):
#     blg = Blog.query.get(id)
#     db.session.merge(blg)
#     db.session.flush()
#     db.session.commit()
#     return redirect ('/admin/blog')



# @admin.route('/blog')
# def blog():
#     blogs = Blog.query.all()
#     return render_template('admin/Blog/blog.html',blogList=blogs)


# @admin.route('/blog/addblog', methods=['GET', 'POST'])
# def addBlog():
#     blogform = BlogForm()
#     if request.method == 'POST':
#         file = blogform.blog_image.data
#         file.save(file.filename)
#         blog = Blog (blog_title = blogform.blog_title.data,blog_image = file.filename,blog_content = blogform.blog_content.data,blog_date = date.today())
#         db.session.add(blog)
#         db.session.commit()
#         return redirect ('/admin/blog')
#     return render_template('Blog/addblog.html', form=blogform)


# @admin.route('/blog/update/<int:id>', methods=['GET', 'POST'])
# def updateBlog(id):
#     blog = Blog.query.get(id)
#     blogform = BlogForm()
#     if request.method == 'POST':
#         file = blogform.blog_img.data
#         file.save(file.filename)
#         newTitle = blogform.blog_title.data
#         newImg = file.filename
#         newContent = blogform.blog_content.data
#         blog.blog_title = newTitle
#         blog.blog_image = newImg
#         blog.blog_content = newContent
#         db.session.merge(blog)
#         db.session.flush()
#         db.session.commit()
#         return redirect ('/admin/blog')
#     return render_template('Blog/update.html', form=blogform, blog=blog)

# @admin.route('/blog/delete/<int:id>')
# def deleteBlog(id):
#     blog = Blog.query.get(id)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect ('/admin/blog')

# --------------------------------------------------Resume--------------------------------------------------------------

@admin.route('/resume' , methods=["POST","GET"])
def resume():
    rsm=Resume.query.all()
    if request.method == "POST":
        rsm=Resume(text=request.form['text'],fullname=request.form['name'])
        db.session.add(rsm)
        db.session.commit()
        return redirect ('/admin/resume')
    return render_template('admin/Resume/resume.html',rsm=rsm)


@admin.route('/resume/<int:id>')
def deleteResume(id):
    rsm = Resume.query.get(id)
    db.session.delete(rsm)
    db.session.commit()
    return redirect ('/admin/resume')


# @app.route('/resume/<int:id>',methods=['GET','POST'])
# def updateResume(id):
#     rsm=Resume.query.get(id)
#     if request.method=='POST':
#         newText=request.form['text']
#         newFullname=request.form['name']
        
#         rsm.text=newText
#         rsm.name=newFullname  
#         db.session.merge(rsm)
#         db.session.flush()
#         db.session.commit()
#         return redirect('/admin/resume')
#     else:
#         return render_template('admin.html',rsm=rsm)







#----------------------------------------------------FOOTER------------------------------------------------------
@admin.route('/footer' , methods=["POST" , "GET"])
def footerpages(): 
    ftr=Footer.query.all()
    if request.method == "POST":
        ftr=Footer(about=request.form["about"],  connect=request.form["connect"],navagation=request.form["navagation"],services=request.form["services"], contact=request.form["contact"])
        db.session.add(ftr)
        db.session.commit()
        return redirect ('/admin/footer')
    return render_template('admin/Footer/footer.html',ftr=ftr)
