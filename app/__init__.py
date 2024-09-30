from flask import Flask, redirect, url_for
from .config.config import Config
from .config.db import db
from flask_migrate import Migrate
from flask_login import LoginManager

from .models.program import *
from .routes.auth import auth_bp
from .routes.admin import admin_bp
from .routes.film import film_bp
from .routes.home import home_bp
from .models.model import User
from .models.model import Role

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()  # Crea tutte le tabelle se non esistono

    # Registra i blueprint
    app.register_blueprint(home_bp, url_prefix='/home')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(film_bp, url_prefix='/film')

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))  # Reindirizza alla pagina di login

    return app
