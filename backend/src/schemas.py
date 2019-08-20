from flask_mongoengine import MongoEngine

db = MongoEngine()

class Photo(db.EmbeddedDocument):
    url = db.StringField()

class Post(db.Document):
    text = db.StringField()
    photos = db. EmbeddedDocumentListField(Photo)