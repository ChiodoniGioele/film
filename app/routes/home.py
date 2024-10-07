
import logging;
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from app.models.program import *
from app.models.model import *
from ..config.db import db

home_bp = Blueprint('home', __name__)
logging.basicConfig(format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@home_bp.route('/')
@login_required
def home():
    if current_user.firstLogin:
        current_user.firstLogin = False
        db.session.commit()
        return render_template('home/firstLogin.html')

    data1 = getData(0, "la1")
    data2 = getData(0, "la2")

    program1 = getPrograms(data1)
    program2 = getPrograms(data2)

    programs = program1 + program2

    user_preferences = current_user.preferences
    preferences_list = [pref.genre for pref in user_preferences]


    preferences_program = {preference: [] for preference in preferences_list}
    for preference in preferences_list:
        for program in programs:
            if any(topic['label'] == preference for topic in program.topics):
                preferences_program[preference].append(program)

    logger.debug(f'Preferences: {preferences_program}')

    return render_template('home/home.html', preferences_program=preferences_program)



@home_bp.route('/la1')
@login_required
def la1():
    data = getData(0,"la1")
    programs = getPrograms(data)
    return render_template('home/channel.html', programs=programs)

@home_bp.route('/la2')
@login_required
def la2():
    data = getData(0,"la2")
    programs = getPrograms(data)
    return render_template('home/channel.html', programs=programs)


@home_bp.route('/submit_preferences', methods=['POST'])
@login_required
def submit_preferences():
    selected_genres = request.form.getlist('genres')

    # Rimuovi le preferenze esistenti per l'utente (se desideri solo le nuove)
    Preferences.query.filter_by(user_id=current_user.id).delete()

    # Salva le nuove preferenze
    for genre in selected_genres:
        preference = Preferences(genre=genre, user_id=current_user.id)
        db.session.add(preference)

    db.session.commit()

    # Aggiorna il flag firstLogin a False
    current_user.firstLogin = False
    db.session.commit()

    flash('Le tue preferenze sono state salvate con successo!', 'success')
    return redirect(url_for('home.home'))