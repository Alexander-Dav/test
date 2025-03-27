import os

SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
SQLALCHEMY_DATABASE_URI = 'sqlite:///tests.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False