from flask import Flask
from flask_mongoengine import MongoEngine
from .schemas import User

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGODB_SETTINGS= {
            "db": "vkfeedfilter"
        },
    )

    db = MongoEngine(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    User(name="rocksfd").save()
    return app