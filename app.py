#flask {{}} 써서 값 바꾸는 법 찾아서 특정 div 바꾸는법 알아보기



from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_mail import Mail, Message
app = Flask(__name__)
import datacon as dc

@app.route('/')
def index():
    return render_template('index.html')

app.config['MAIL_SERVER'] = 'smtp.naver.com'
app.config["MAIL_PORT"] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/process_login/')
def process_login():
    email=request.values.get('email')
    pw=request.values.get('pw')
    

@app.route('/signup/')
def signupk():
    return render_template('signup.html')

@app.route('/process_signup/', methods=['GET', 'POST'])
def process_signup():
    if request.method=='get':
        return redirect('/process_signup/')
    elif request.method=='post':
        suname=request.form.get('sign-uname')
        semail=request.form.get('sign-email')
        spw=request.form.get('sign-pw')
        dc.update_data(suname,semail,spw)
        except:                                      #중복된 mail 없을때
            return render_template('/login/')       
        try:                                        #mail이 중복될때
            return render_template('fail_signup.html')  #signup 화면과 똑같은데 mail칸에 중복이라고 표시해둔 화면 
        
    

# @app.route('/check_mail/', methods=['GET', 'POST'])
# def mail():
#     try:
#         address=request.values.get('emailAddress')
#         return redirect('/right_email/')

#     except:
#         return 

#         address=request.values.get('emailAddress')
#         address=request.values.get('emailAddress')
#         msg = Message('Hello', sender='chamgf5247@naver.com', recipients=[address])
#         msg.body = 'Hello Flask message sent fro Flask-Mail'
#         Mail(app).send(msg)
#         return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
