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
    

@app.route('/signup/' ,methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    elif request.method=='POST':
        suname=request.form.get('sign-uname')
        semail=request.form.get('sign-email')
        spw=request.form.get('sign-pw')
        try :
            if suname!='' and semail!='' and spw!='':
                if dc.check_uname(suname)==False and dc.check_mail(semail)==False:
                    dc.add_data(suname,semail,spw)
                    return redirect('/login/')
                else:
                    return render_template('signup.html', hidden='off' ,text='Duplicate name or email. Please enter a different value.')
            else:
                return render_template('signup.html', hidden='off', text="Do not allow spaces. Please enter a value.")     
        except:
            return render_template('signup.html', hidden='off', text="Signup failed Please try again!")
        #     return redirect('/login/')
        #     return render_template('fail_singup.html')    
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
