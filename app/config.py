import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Config:
    MONGO_URI = 'mongodb://localhost:27017/mydatabase'
    DEBUG = os.getenv("DEBUG")
    SECRET_KEY = os.getenv("SECRET_KEY")
    
class DevelopmentConfig(Config):
    DEBUG = False

class ProductiontConfig(Config):
    pass