from flask import Blueprint, render_template
from flask_login import login_required, current_user
from dotenv import load_dotenv

load_dotenv()

film_bp = Blueprint('film', __name__)

@film_bp.before_request
@login_required
def before_request():
    pass
