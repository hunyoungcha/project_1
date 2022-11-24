#flask {{}} 써서 값 바꾸는 법 찾아서 특정 div 바꾸는법 알아보기
#txt에 데이터 추가, 삭제 될거고
#python 파일 하나 만들어서 전처리 해서 넘어오는 걸로



from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_mail import Mail, Message
app = Flask(__name__)



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
    else:
        suname=request.form.get('sign-uname')
        semail=request.form.get('sign-email')
        spw=request.form.get('sign-pw')

        data=open('database.txt', 'r')
        
    

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
