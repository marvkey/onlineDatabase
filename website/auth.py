from flask import Blueprint,render_template,flash,request,redirect,url_for

auth = Blueprint("auth",__name__)
@auth.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")

@auth.route("/signup",methods=["GET","POST"])
def signup():
    return render_template("signUp.html")
