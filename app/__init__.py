from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#create database object globally

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    
    app.config['SECRET_KEY']='supersecret'
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    db.__init__(app)
    
    from app import models
    
    from app.routes.auth import auth_bp
    from app.routes.auth import tasks_bp
    
    app.register_blueprint(auth_bp,url_prefix="/auth")
    app.register_blueprint(tasks_bp,url_prefix="/tasks")
    
    return app
    