from flask import Flask, redirect, url_for
from .config.config import Config
from .config.db import db
from flask_migrate import Migrate
from flask_login import LoginManager
from .routes.auth import auth_bp  # Importa il blueprint auth
from .routes.admin import admin_bp
from .routes.film import film_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Importa User qui per poterlo usare nel user_loader
    from .models.model import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        from .models.model import Role  # Importa il modello Role se necessario
        db.create_all()  # Crea tutte le tabelle se non esistono

    # Registra i blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(film_bp, url_prefix='/film')

    # Aggiungi la route per la radice
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))  # Reindirizza alla pagina di login

    return app
