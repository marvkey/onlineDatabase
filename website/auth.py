from flask import Blueprint,render_template,flash,request,redirect,url_for
from flask_login import login_user, logout_user, login_required,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .userData import User
from . import db

auth = Blueprint("auth",__name__)
@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):#if the hash password equals the passowrd in text
                flash("logged in!",category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Password is incorrect",category='error')
        else:
            flash("email is not valid",category='error')
    return render_template("login.html",user=current_user)#letting us use user in base template



@auth.route("/signup",methods=["GET","POST"])
def signup():
    if request.method =='POST':
        email = request.form.get("email")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        username = request.form.get("username")
        password1 = request.form.get("password1") 
        password2= request.form.get("password2")
        
        email_exist = User.query.filter_by(email=email).first()
        if(email_exist):
            flash("The email address registered with an account",category="error")
        elif(len(firstname)<=0):
            flash("Please enter a first name ",category="error")
        elif(len(lastname)<=0):
            flash("Please enter a last name",category="error")
        elif(len(lastname)<=0):
            flash("Please enter a User name",category="error")
        elif(len(password1)<5):
            flash("Passeord has to be atleast 5 character long",category="error")
        elif(password1 !=password2):
            flash("Password do not match",category="error")
        else:
            new_user =User(email=email,firstname=firstname,lastname=lastname,username=username,password=generate_password_hash(password1,method ="sha256"))
            db.session.add(new_user)# ready to be in database
            db.session.commit()#adds to database
            login_user(new_user,remember=False)
            flash("User Created",category='success')
            return redirect(url_for('views.home'))
    return render_template("signUp.html",user=current_user)
@auth.route("/logout")
@login_required # only access the page when logged in
def logout():
    logout_user()
    return redirect(url_for("views.home"))

