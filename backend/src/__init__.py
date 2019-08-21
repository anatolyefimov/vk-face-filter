from flask import Flask
from flask_mongoengine import MongoEngine
from .updater import update_by_timeout
from .schemas import Post
from flask import jsonify

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGODB_SETTINGS= {
            "db": "vkfeedfilter"
        },
    )

    from .schemas import db, Post, Photo
    db.init_app(app)

    @app.route('/')
    def give_post():
        posts = [{ "text": post.text, "photos": post.photos} for post in Post.objects]
        return jsonify(posts)
    
    update_by_timeout()
    
    return app