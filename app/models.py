from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    department = db.Column(db.String(50))
    must_change_password = db.Column(db.Boolean, default=False)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    title = db.Column(db.String(200), nullable=False)
    timer_enabled = db.Column(db.Boolean, default=False)
    timer_seconds = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))
    text = db.Column(db.Text, nullable=False)
    options = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.String(10), nullable=False)

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))
    score = db.Column(db.Float, nullable=False)
    time_spent = db.Column(db.Integer)  # seconds
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)