import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///menudatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
