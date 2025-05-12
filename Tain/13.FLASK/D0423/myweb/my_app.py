from flask import Flask
APP=Flask(__name__)
@APP.route('/')
def index():
    return "<h1><font color='blue'>Hello MyWeb~!!</font><h2>"
@APP.route("/hello",endpoint='hello_page')
def hello():
    return '바보보'
@APP.route("/<msg>")
def messagee(msg):
    return f"나는 바보: {msg}"
@APP.route("/userinfo")
def userinfo(msg):
    return APP.redirect('/')
if __name__=='__main__':
    APP.run()