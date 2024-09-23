from flask import Flask
from .config.config import Config
from .config.db import db
from flask_migrate import Migrate



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from .models.model import User  # Importa il modello User
        db.create_all()  # Crea tutte le tabelle se non esistono
        from .routes.route import some_route  
        app.register_blueprint(some_route)  

    return app
