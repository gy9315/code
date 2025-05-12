from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# DB관련 설정
import config
# DB를 제어하기 위한 인스턴스
DB=SQLAlchemy()
MIGRATE=Migrate()
def create_app():
    APP=Flask(__name__)
    # DB 관련 초기화 설정: config.py 파일 읽어서 웹서버에 설정 구성
    APP.config.from_object(config)
    # DB초기화 및 연동
    DB.init_app(APP)
    MIGRATE.init_app(APP,DB)
    from .models import models
    from .views import main_view
    from .views import user_view,question_view,detail_view,answer_view
    APP.register_blueprint(main_view.bp)
    APP.register_blueprint(user_view.user_bp)
    APP.register_blueprint(question_view.question_bp)
    APP.register_blueprint(detail_view.detail_bp)
    APP.register_blueprint(answer_view.answer_bp)
    return APP