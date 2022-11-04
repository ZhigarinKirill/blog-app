from datetime import datetime
from flask_mongoengine import MongoEngine


db = MongoEngine()


class Post(db.Document):
    title: str = db.StringField()
    content: str = db.StringField()
    publish_date: datetime = db.DateTimeField(default=datetime.utcnow)
    author: str = db.StringField()
