from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.program import *

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
@login_required
def home():
    data = getData(0)
    programs = getPrograms(data)
    return render_template('home/home.html', programs=programs)
