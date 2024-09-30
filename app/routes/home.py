from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.program import *

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
@login_required
def home():
    data = getData(0,"la1")
    programs = getPrograms(data)
    return render_template('home/home.html', programs=programs)

@home_bp.route('/la1')
@login_required
def la1():
    data = getData(0,"la1")
    programs = getPrograms(data)
    return render_template('home/home.html', programs=programs)

@home_bp.route('/la2')
@login_required
def la2():
    data = getData(0,"la2")
    programs = getPrograms(data)
    return render_template('home/home.html', programs=programs)
