from flask import Flask,jsonify,session
import os
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from flask_session import Session
from flask_cors import CORS, cross_origin

from flask_smorest import Api
import Models
from db import db

# from Resources.errors import blp as errors_blueprint
from Resources.auth import blp as auth_blueprint
from Resources.error import blp as error_blueprint
from Resources.employer import blp as employer_blueprint
app=Flask(__name__)

def create_app(db_url=None):
    # register the blueprints with the api
    app.config["PROPAGATE_EXCEPTIONS"]=True   #This is a Flask configuration that says that if there is an exception that occurs hidden inside an extension of Flask to propagate into the main app so that we can see it.
    app.config["API_TITLE"]="Stores REST Api"
    app.config["API_VERSION"]="V1"
    app.config["OPENAPI_VERSION"]="3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"  # tells flask_smorest wher the root of the api is
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist"
    app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")  # have to enter a connection string
    #  "sqlite:///data.db"  this is a valid sql lite connections string that creates a file
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'imkishor16@gmail.com'
    app.config['MAIL_PASSWORD'] = 'JETRAY@403'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    # app.config['SESSION_COOKIE_SECURE'] = True  # Use 'True' for HTTPS
    app.config['SESSION_COOKIE_SAMESITE'] = 'None' 

    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'secretkeyforSession'
    
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # mail = Mail()
    # mail.init_app(app)
    # mail = Mail(app)
    # mail=Mail().init_app(app)
    sender = 'imkishor16@gmail.com'

    # session = Session()
    # session.init_app(app)
    
    Session(app)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.secret_key = 'proctor_app'


    YOUR_DOMAIN = 'http://localhost:5000'
    
    db.init_app(app) # it initializes the Flask SQLAlchemy extension,giving it our Flask app so that it can connect the Flask app to SQLAlchemy.
    with app.app_context(): # this funtions runs first when our app starts and creates the tables 
        db.create_all()

        
    api=Api(app)
    
    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(error_blueprint)
    app.register_blueprint(employer_blueprint)
    
    return app





























































# def create_app(db_url=None):
#     app.config["PROPAGATE_EXCEPTIONS"]=True   #This is a Flask configuration that says that if there is an exception that occurs hidden inside an extension of Flask to propagate into the main app so that we can see it.
#     app.config["API_TITLE"]="Stores REST Api"
#     app.config["API_VERSION"]="V1"
#     app.config["OPENAPI_VERSION"]="3.0.3"
#     app.config["OPENAPI_URL_PREFIX"]="/"  # tells flask_smorest wher the root of the api is
#     app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
#     app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist"
#     app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")  # have to enter a connection string
#     #  "sqlite:///data.db"  this is a valid sql lite connections string that creates a file
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     app.config["PROPAGATE_EXCEPTIONS"] = True
    
#     db.init_app(app) # it initializes the Flask SQLAlchemy extension,giving it our Flask app so that it can connect the Flask app to SQLAlchemy.
#     api=Api(app)  
    
#     with app.app_context(): # this funtions runs first when our app starts and creates the tables 
#         db.create_all()
        
#     app.config["JWT_SECRET_KEY"]="dsfkl"
#     # app.config["JWT_SECRET_KEY"]=secrets.SystemRandom().getrandbits(128)
#     jwt=JWTManager(app)
    
#     @jwt.token_in_blocklist_loader
#     def check_if_token_in_blocklist(jwt_header, jwt_payload):
#         return jwt_payload["jti"] in BLOCKLIST
#     @jwt.revoked_token_loader
#     def revoked_token_callback(jwt_header, jwt_payload):
#         return (
#             jsonify(
#                 {"description": "The token has been revoked.", "error": "token_revoked"}
#             ),
#             401,
#         )
#     #Error handling for jwt
#     @jwt.expired_token_loader
#     def expired_token_callback(jwt_header, jwt_payload):
#         return (
#             jsonify({"message": "The token has expired.", "error": "token_expired"}),
#             401,
#         )
#     @jwt.invalid_token_loader
#     def invalid_token_callback(error):
#         return (
#             jsonify(
#                 {"message": "Signature verification failed.", "error": "invalid_token"}
#             ),
#             401,
#         )
#     @jwt.unauthorized_loader
#     def missing_token_callback(error):
#         return (
#             jsonify(
#                 {
#                     "description": "Request does not contain an access token.",
#                     "error": "authorization_required",
#                 }
#             ),
#             401,
#         )
#     @jwt.additional_claims_loader
#     def add_claims_to_jwt(identity): #  is a function that runs every time you create an access token/a JWT.
#         if identity==1:
#             return {"is_admin":True}
#         else:
#             return {"is_admin":False}    
#     return app
    