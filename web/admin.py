from .models import User
from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/login')
def login():
    return 'Login'


@admin.route('/signup')
def signup():
    return 'Signup'


@admin.route('/logout')
def logout():
    return 'Logout'
