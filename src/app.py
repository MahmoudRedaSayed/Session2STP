

from random import random
from flask import Flask, redirect, render_template,request,session,url_for
import os

repo_path = os.path.abspath(os.path.dirname(__name__))

template_dir = os.path.join(
        repo_path,  'templates'  # location of front end pages
    )
print(template_dir)
print(repo_path)
static_dir = os.path.join(
        repo_path,  'static'  # location of front end pages
    )
# create flask app
app = Flask(__name__, template_folder=template_dir,static_folder=static_dir)
# use it to the session
app.secret_key=os.urandom(32)

# The route of the Home page
#Home can take two routes but like / but it must have  paramertar name
@app.route("/home/<name>")
def home(name):
    return render_template("home.html",name=name)

#The login page will render the login.html page and the form will send the data to the profile page to check it
#The route of the login page
@app.route("/")
@app.route("/login")
def LoginPage():
    # check if the user logged in or not by using the session
    if "Id" not in session :
        return render_template("login.html")
    else:
        return redirect("/home")
#we will use the session to check if the user still in the site or logged out (session like dic but dynamic)
#the profile page will check the data comes from the login page if the data is correct it will show it to the user else will redirect to the error page
# The route of the profile page
@app.route("/profilecheckdata",methods=["POST"])
def ProfileCheckdata():
    #the data of the users like  database
    users_data=[
                (1,"Ahmed Emad","0123456789","AhmedEmad@gmail.com","1245"),
                (2,"Ahmed Salah","0123456789","AhmedSalah@gmail.com","2586"),
                (3,"Mahmoud Reda","01102306392","MahmoudReda@gmail.com","0110"),
                (4,"Remon","0123456789","RemonSahebSalah@gmail.com","2586"), 
                (5,"Panda","0123456789","MohamedKhald@gmail.com","1245")
                ]
    #get the data from the login page using the request 
    email=request.form.get("Email")
    password=request.form.get("Password")
    #put the data into tuple
    user_Data=tuple([email,password])

    for i in users_data:
        if user_Data==i[3:]:
            session["Id"]=i[0]
    if "Id" in  session :
        return redirect(url_for('Profile'))
    else:
        return "Error"
@app.route("/profile")
def Profile():
    #the data of the users like  database
    users_data=[
                (1,"Ahmed Emad","0123456789","AhmedEmad@gmail.com","1245"),
                (2,"Ahmed Salah","0123456789","AhmedSalah@gmail.com","2586"),
                (3,"Mahmoud Reda","01102306392","MahmoudReda@gmail.com","0110"),
                (4,"Remon","0123456789","RemonSahebSalah@gmail.com","2586"), 
                (5,"Panda","0123456789","MohamedKhald@gmail.com","1245")
                ]
    for i in users_data:
        if session["Id"]==i[0]:
            Datals=i
            break
    return render_template("profile.html",Data=Datals)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# error handler to handle the error page
@app.errorhandler(404)
def error_404(e):
    return render_template("Error.html"),404

if __name__=="__main__":
    app.run(debug=True,port="3000")