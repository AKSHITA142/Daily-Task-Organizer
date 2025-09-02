from flask import Blueprint,render_template,request,redirect,url_for,flash,session

auth_bp=Blueprint('auth',__name__)
auth_bp.secret_key='supersecret'

users={}

@auth_bp.route('/sign_up',methods=["GET","POST"])
def sign_up():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('paasword')
        users[username]=password
        flash("Dear {username} Now you can Login")
        return redirect(url_for(login))
    return render_template("sign-up.html")

@auth_bp.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username in users and users["useranme"]==password:
            session["user"]=username
            flash("Dear {username} You have Succesfully Login!!")
        flash("Invalid username or password! please try it again!!")
    return render_template("login.html",name=username)

@auth_bp.route('/logout')
def logout(): 
    session.pop("user",None)
    flash("logged out")
    return redirect(url_for(auth_bp.login))
        