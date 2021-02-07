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
        rand=random.randint(1, 9999)
        f = request.files['image']
        newName=f"blogfile{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 
        Homm=Home(title=request.form["title"], text=request.form["text"],image=filePath)
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

#------------------------------------------------------ABOUT----------------------------------------------------------


# -------Skill------
@admin.route('/skill' , methods=["GET","POST"])
def skillspage():
    skl=Skill.query.all()
    if request.method == "POST":
        skl=Skill(percent=request.form["percent"], name=request.form["name"],title=request.form["title"])
        db.session.add(skl)
        db.session.commit()
        return redirect('/admin/skill')
    return render_template('/admin/Skill/skill.html',skl=skl)


@admin.route('/skill/<int:id>')
def deleteSkill(id):
    skl = Skill.query.get(id)
    db.session.delete(skl)
    db.session.commit()
    return redirect ('/admin/skill')
    

# -------About---------

@admin.route('/about' , methods=["GET","POST"])
def aboutPages():
    skl=Skill.query.all()
    abt=About.query.all()
    if request.method == "POST":
        rand=random.randint(1, 9999)
        f = request.files['image']
        newName=f"blogfile{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 

        abt=About(text=request.form["text"],title=request.form["title"],skill_id=request.form["skill_id"],image=filePath)
        db.session.add(abt)
        db.session.commit()
        return redirect('/admin/about')
    return render_template('/admin/About/about.html',skl=skl,abt=abt)


@admin.route('/about/<int:id>')
def deleteAbout(id):
    abt = About.query.get(id)
    db.session.delete(abt)
    db.session.commit()
    return redirect ('/admin/about')





#------------------------------------------------------- Portfolio-------------------------------------------------------
# -------Category------
@admin.route('/category' , methods=["GET","POST"])
def categoriespages():
    ctg=Category.query.all()
    if request.method == "POST":
        ctg=Category(name=request.form["name"], title=request.form["title"])
        db.session.add(ctg)
        db.session.commit()
        return redirect('/admin/category')
    return render_template('/admin/Category/category.html',ctg=ctg)


@admin.route('/category/<int:id>')
def deleteCategory(id):
    ctg = Category.query.get(id)
    db.session.delete(ctg)
    db.session.commit()
    return redirect ('/admin/category')
    

# -------Portfolio---------

@admin.route('/portfolio' , methods=["GET","POST"])
def portfoliopages():
    ctg=Category.query.all()
    prt=Portfolio.query.all()
    if request.method == "POST":
        rand=random.randint(1, 9999)
        f = request.files['image']
        newName=f"blogfile{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 

        prt=Portfolio(title=request.form["title"],category_id=request.form["category"],image=filePath)
        db.session.add(prt)
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('/admin/Portfolio/portfolio.html',prt=prt,ctg=ctg)


@admin.route('/portfolio/<int:id>')
def deletePortfolio(id):
    prt = Portfolio.query.get(id)
    db.session.delete(prt)
    db.session.commit()
    return redirect ('/admin/portfolio')
    











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
        today = date.today()
        rand=random.randint(1, 9999)
        f = request.files['image']
        newName=f"blogfile{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 
        blg=Blog(text=request.form['text'],title=request.form['title'],image=filePath,time=today)
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




# --------------------------------------------------Resume--------------------------------------------------------------

@admin.route('/resume' , methods=["POST","GET"])
def resume():
    rsm=Resume.query.all()
    if request.method == "POST":
        rand=random.randint(1, 9999)
        f = request.files['image']
        newName=f"blogfile{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 
        
        rsm=Resume(text=request.form['text'],fullname=request.form['name'],image=filePath)
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
