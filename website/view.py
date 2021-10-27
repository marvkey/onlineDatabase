from website import auth
from flask import Blueprint,render_template,flash,request,redirect,url_for,Flask,send_file
from flask_login import login_required, current_user
from io import StringIO
from . import db
from .userData import SavedItem
views = Blueprint("views",__name__)
@views.route("/")
@views.route("/home",methods=["GET","POST"])
def home():
    files=SavedItem.query.all()
    return render_template("home.html",user=current_user,files=files)


@views.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method =='POST':
        file = request.files['file']
        newFile = SavedItem(file=file.read(), name=file.filename,Description="this is a text file ",author=current_user.id)
        db.session.add(newFile)
        db.session.commit()
        flash(f"file loaded:{file.filename}",category='success')
    return render_template("create_file.html",user=current_user)

@views.route('/download/<file>', methods = ['POST','GET'])
def download(file):
    #file = request.files['file']
    #file.filename
     
   # string = 
    return redirect(url_for("views.home"))