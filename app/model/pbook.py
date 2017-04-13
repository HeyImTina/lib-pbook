# coding:utf-8
from app.model import db
from sqlalchemy import UniqueConstraint
from datetime import datetime


class Pbook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    location = db.Column(db.String(100))
    category = db.Column(db.String(100))
    ibsn = db.Column(db.String(15))
    publish = db.Column(db.String(50))
    user_id = db.Column(db.Integer)
    book_time = db.Column(db.DateTime())
    created_time = db.Column(db.DateTime(), default=datetime.now)

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "location": self.location,
            "category": self.category,
            "ibsn": self.ibsn,
            "publish": self.publish,
        }
