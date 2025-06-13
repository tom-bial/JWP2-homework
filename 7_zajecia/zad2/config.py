import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app_teachers.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False