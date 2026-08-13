from flask import Flask
from .config import Config
from app.Extensions import db,login_manager,migrate

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.query.get(int(user_id))
    migrate.init_app(app,db)

    from . import models
    from .routes.auth import auth
    from .routes.post import post
    app.register_blueprint(auth)
    app.register_blueprint(post)
    return app

