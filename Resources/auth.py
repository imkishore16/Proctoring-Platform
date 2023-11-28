from flask import Flask ,request , render_template,url_for,redirect,flash,session
from passlib.hash import pbkdf2_sha256
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required, get_jwt
from Models.user import UserModel
from db import db
from sqlalchemy.exc import SQLAlchemyError
import math,random
import pickle
from flask_mail import Mail, Message


def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(6):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP

blp = Blueprint("Auth", "auth", description="Operations on authentication")
@blp.route("/register", methods=['POST', 'GET'])
def register():
    print("from register")
    print(session.get("username"))
    if request.method == "POST":
        user_data = request.form.to_dict()
        print(user_data)
        try:
            # if UserModel.query.filter(UserModel.email == user_data["email"]).first():
            #     abort(400, message="A user with that email already exists")
            user = UserModel(
                email=user_data["email"],
                name=user_data["name"],
                password=pbkdf2_sha256.hash(user_data["password"]),
                image_data=user_data["image_hidden"])
            # from app import app
            sender="imkishor16@gmail.com"
            sesOTP = generateOTP()
            session["sesOTP"] = sesOTP
            session.modified = True
            
            session["email"]=user_data["email"],
            session["name"]=user_data["name"],
            session["password"]=pbkdf2_sha256.hash(user_data["password"]),
            session["user_type"]=user_data["user_type"]
            session["image_data"]=user_data["image_hidden"]
            # mail = Mail(app)
            # msg1 = Message('Proctor - OTP Verification', sender=sender, recipients=[user_data["email"]])
            # msg1.body = "New Account opening - Your OTP Verfication code is " + sesOTP + "."
            # mail.send(msg1)
            return redirect(url_for('Auth.verifyEmail'))
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(404, message=str(e))
    return render_template("register.html")
        

@blp.route("/verifyEmail" , methods=["POST","GET"])
def verifyEmail():
    if request.method=="POST":
        # OTP=request.form('eotp')
        sesOTP=session.get("sesOTP")
        if(sesOTP==sesOTP):
            try:
                user = UserModel(
                    email=session.get("email"),
                    name=session.get("name"),
                    password=session.get("password"),
                    user_type=session.get("user_type"),
                    image_data=session.get("image_data")
                )
                db.session.add((user))
                db.session.commit()
                flash("Thanks for registering! You are sucessfully verified!.")
                return redirect(url_for('login'))
            except SQLAlchemyError as e:
                abort(500,message=str(e))
                # return redirect(url_for('Auth.register'))
        else:
            print("incoredct")
            # return redirect(url_for("Auth.register.html"))
            return render_template("verifyEmail.html",error="Incorrect OTP")
    return render_template("verifyEmail.html")
                

@blp.route("/",methods=["POST","GET"])
def login():
    session["username"]="John Wick"
    if request.method=="POST":
        user_data = request.form.to_dict() 
        try:
            # if UserModel.query.filter(UserModel.email==user_data["email"]).first():
            #     abort(400,message="A user with that username already exists")
            user=UserModel(
                email=user_data["email"],
                password=pbkdf2_sha256.hash(user_data["password"]),
                user_type=user_data["user_type"],
                image_data=user_data["image_hidden"]
            )
            if user and pbkdf2_sha256.verify(user_data["password"],user.password):
                # access_token=create_access_token(identity=user.id)
                # return access_token # in the jwt the user's id will be stored under the key "sub" 
                return redirect(url_for("homepage"))
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(404, message="Internal Server Error")
    return render_template("login.html")
    
    # user= UserModel.query.filter(UserModel.name==user_data["name"]).first()
    # abort(401,message="Invalid credentials")
        
@blp.route("/logout")
def logout(self):
    pass

# @blp.route("/employeer_index",methods=["POST","GET"])
# # @user_role_employeer
# def employeer_index():
#     return render_template('employeer_index.html')