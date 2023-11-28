from app import create_app

from flask import Flask,session
app=create_app()

# app=Flask(__name__)

# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SECRET_KEY'] = 'secretkeyforSession'

# @app.route("/")
# def login():
#     session["user"]="kishore"
#     return "<h1>tata</h1>"
    
# @app.route("/register")
# def register():
#     user=session.get("user")
#     print(user)
#     return "<h1>{{user}}</h1>"
    


if __name__=='__main__':
    app.run(debug=True)