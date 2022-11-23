#signup 폼 데이터 못받아 오고 계속 오류 뜸 해결 해야함


from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_mail import Mail, Message
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

app.config['MAIL_SERVER'] = 'smtp.naver.com'
app.config["MAIL_PORT"] = 465
app.config['MAIL_USERNAME'] = 'chamgf5247'
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
    uname=request.values.get('sign-uname')
    email=request.values.get('sign-email')
    pw=request.values.get('sign-pw')
    return uname ,email, pw

    # data=open('database', 'a')
    # data.write(f'{uname} {email} {pw}')
    # return redirect('/login/')


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
