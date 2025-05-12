from flask import Blueprint
user_bp=Blueprint('user',__name__,template_folder='templates',url_prefix='/user')
@user_bp.route('/')
def index():
    return '바보'