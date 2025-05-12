""" 
필요한 것
저장한 모델
models안의 mymodel.py
저장한 vocab

"""


from flask import Flask, request, render_template
import torch
import pickle
from models.mymodel import *

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)
@app.route("/", methods=["GET", "POST"])
def index():
    pred=None 
    proba=None
    if request.method == "POST":
        input_text = request.form.get("text", "")
        pred,proba=test(LSTModel,'./LSTModel.pkl',word2vec,input_text,vocab)
    return render_template("index.html", prediction=f'{pred}, 예측확률: {proba}%')
if __name__ == "__main__":
    app.run(debug=True)