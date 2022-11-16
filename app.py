#welcome 페이지 넘어갈때 id pw 가져가는 법
#welcome 페이지에 welcome{id} 형식 만들기



from flask import Flask, render_template, request
import os
import database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    id=request.form['id']
    pw=request.form['pw']
    
    if request.method=='GET':
        render_template('fail_login.html')
    elif request.method=='POST':
        if database.getKey(id) and database.getValue(pw) :
            return render_template('welcome.html', id=id, pw=pw,)
        else:
            return render_template('fail_login.html')

app.run()