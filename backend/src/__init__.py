from flask import Flask
from flask import Response
from flask_mongoengine import MongoEngine
from .updater import update_by_timeout
import json

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGODB_SETTINGS= {
            "db": "vkfeedfilter"
        },
    )

    from .schemas import db, Post
    db.init_app(app)

    update_by_timeout()

    @app.route('/')
    def give_post():
        posts = [{ "text": post.text, "photos": post.photos} for post in Post.objects]
        js = json.dumps(posts)

        res = Response(js, status=200, mimetype='application/json')
        res.headers['Access-Control-Allow-Origin'] = '*'

        return res
    
    @app.route('/hello')
    def  hello():
        return "hello"
    
    return app