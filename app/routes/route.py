from flask import Blueprint, render_template

# Crea un blueprint per le route
some_route = Blueprint('some_route', __name__)

@some_route.route('/')
def index():
    return render_template('index.html')  # Assicurati di avere un template chiamato index.html
