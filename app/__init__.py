from flask import Flask
from app.db import mongo  #to avoid circular import 
from app.routes import register_routes
from app.config import Config , DevelopmentConfig , ProductiontConfig
import os
from dotenv import load_dotenv

load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    mongo.init_app(app)

    register_routes(app)

    return app
