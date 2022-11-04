from flask import Flask
from routes.post import post_pages
from routes.index import index_pages


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/db.py')

    from models import db
    db.init_app(app)

    app.register_blueprint(post_pages, url_prefix='/posts')
    app.register_blueprint(index_pages)

    return app
