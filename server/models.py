from flask_mongoengine import MongoEngine
import datetime

db = MongoEngine()

class User(db.Document):
    name = db.StringField(required=True, max_length=8)
    email = db.EmailField(required=True)
    password = db.StringField(required=True, max_length=8)
    date_created = db.DateTimeField(default=datetime.datetime.utcnow())

