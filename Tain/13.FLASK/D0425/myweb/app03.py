from flask import Flask,render_template,make_response,request,url_for,session
APP=Flask(__name__)
# Flask 세선을 위한 시크릿 키
# os.urandom(24):암호적으로 안전한 랜덤 바이트를 생성
APP.secret_key=f'super-secret-key-756574234234'

## =================================================
@APP.route('/')
def index():
    if 'username' in session:
        user_name=session.get('username')
        return render_template('user_page.html',name=user_name)
    else:
        return render_template('login.html')

if __name__=='__main__':
    APP.run()