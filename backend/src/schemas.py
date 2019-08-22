from flask_mongoengine import MongoEngine

db = MongoEngine()

class Post(db.Document):
    text = db.StringField()
    photos = db.ListField(db.StringField())