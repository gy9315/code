from flask import Flask,render_template,make_response,request
APP=Flask(__name__)
## view 기능 함수들
## =================================================
## 함수이름: index
## 함수기능: http://127.0.0.1:5000/요청처리 view 함수
## 반환결과: html string
## =================================================
@APP.route('/')
def index():
    return '바보'
## view 기능 함수들
## =================================================
## 함수이름: hello
## 함수기능: http://127.0.0.1:5000/hello 요청처리 view 함수
## 반환결과: html string
## =================================================
@APP.route('/set-cookie')
def set_cookie():
    resp=make_response('쿠기가 설정되었습니다')
    resp.set_cookie('username','K',max_age=60*60)
    return resp
@APP.route('/get-cookie')
def get_cookie():
    username=request.cookies.get('username')
    return f'쿠키값: {username}' if username else '쿠기없음'

@APP.route('/del-cookie')
def del_cookie():
    resp=make_response('쿠기가 삭제되었습니다.')
    resp.set_cookie('username',expires=0)
    return resp

if __name__=='__main__':
    APP.run()