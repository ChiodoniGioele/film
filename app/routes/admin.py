from flask import Blueprint
from flask_login import login_required, current_user
from ..helper.decotators import user_has_role

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
@login_required
@user_has_role('admin')
def default():
    return 'Admin Home'

