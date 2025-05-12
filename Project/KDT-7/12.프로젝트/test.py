from flask import Blueprint, request, render_template,jsonify
from sqlalchemy import select
from datetime import datetime
from base_model_utils import *
from app.db_utils import get_db_connection
from app.recommender.transfer_model import TransferRecommender
from app import db
import json


model_bp = Blueprint('model', __name__, url_prefix='/model')

# 추천 모델 준비
recommender = None
corpus_data = []
@model_bp.route('/')
def index():
    return '바보'
def calculate_d_day(end_date):
    """
    마감일로부터 남은 일수 계산 (D-Day 형식)
    """
    today = datetime.today().date()
    d_day = (end_date - today).days
    if d_day > 0:
        return f"D-{d_day}"
    elif d_day == 0:
        return "D-Day"
    else:
        return "마감"

@model_bp.route('/result_transfer', methods=['POST'])
def model_recommend():
    data = request.get_json()  # json으로 받기
    nickname = data.get('nickname')
    keyword = data.get('keyword')
    contests = data.get('contests')
    model=Predict_name(contests,'./word2vec.model')
    recommended_contests=model.pred(keyword,number=5)
    if not contests or not keyword:
        return "Invalid input", 400
    # 결과를 템플릿에 넘기기
    return render_template('result_transfer.html', results=recommended_contests, name=nickname)