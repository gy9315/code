from flask import Flask
def create_app():
    APP=Flask(__name__)
    from .views import main_view
    from .views import user_view
    APP.register_blueprint(main_view.bp)
    APP.register_blueprint(user_view.user_bp)
    return APP