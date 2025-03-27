from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(template_mode='bootstrap3')

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    
    from . import models, routes, admin as admin_views, auth
    admin_views.configure_admin(admin)
    
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)
    
    return app