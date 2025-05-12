from flask import Flask,render_template
APP=Flask(__name__)
## view 기능 함수들
## =================================================
## 함수이름: index
## 함수기능: http://127.0.0.1:5000/요청처리 view 함수
## 반환결과: html string
## =================================================
def index():
    return render_template('index.html')
## view 기능 함수들
## =================================================
## 함수이름: hello
## 함수기능: http://127.0.0.1:5000/hello 요청처리 view 함수
## 반환결과: html string
## =================================================
def hello():
    return "hello from add_url_rule!"

APP.add_url_rule('/',endpoint='index_page',view_func=index, methods=['GET'])
APP.add_url_rule('/hello',endpoint='hello_page',view_func=hello, methods=['GET'])
if __name__=='__main__':
    APP.run()