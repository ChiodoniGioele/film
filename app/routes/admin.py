from flask import Blueprint
from flask_login import login_required, current_user
from ..decotators import user_has_role

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def default():
    return 'Admin Home'

@admin_bp.route('/dashboard')
@login_required
@user_has_role('admin')
def dashboard():
    return 'Admin Dashboard'
