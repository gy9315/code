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
@APP.route('/login',methods=['POST'])
def login():
    username=request.form.get('username')
    if username:
        session['username']=username
        return APP.redirect(url_for('index'))
@APP.route('/logout')
def logout():
    session.pop('username',None)
    return APP.redirect('/')
@APP.route('/check-session')
def check_session():
    user=session.get('username')
    if user:
        return f'현재 로그인 사용자: {user}'
    else:
        return '로그인한 사용자가 없습니다.'
if __name__=='__main__':
    APP.run()