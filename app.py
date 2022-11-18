#로그인 구현 되면 임시 디비 만들어서 거기에 저장해둘것
#로그인 성공 실패 페이지 만들어서 성공하면 홈페이지, 실패하면 다시 시도


from flask import Flask, render_template, request, session, url_for, redirect
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/login_confirm/', methods=['POST'])
def login_confirm():
    id= request.form['id']
    pw= request.form['pw']
    if (id=='admin' and pw=='admin') or (id=='guest' and pw=='guest'):
        session['id']=id
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 
