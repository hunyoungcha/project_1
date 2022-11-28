#home.html 디자인 고치기
#input time으로 받은 값 받아와서 if realtime==inputtime 하면 mail보내기
#database에 uname email pw 뒤에 wanttime 하나 하고
#기존에 데이터 가져오던것들은 다 [:2]로 고쳐서 받아오기



from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_mail import Mail, Message
import datacon as dc

app = Flask(__name__)
app.secret_key="My_Key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<uname>/',methods=['GET','POST'])
def home(uname):
    if request.method=='GET':
        return render_template('home.html', name=uname)
    elif request.method=='POST':
        time=request.form.get('time')
        return time
    #time 설정 안된 계정은 다 08:00으로
    #dc.add_time()으로 계정 정보 뒤에 time 추가 하기

@app.route('/delete/<uname>')
def delete(uname):
    return uname

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        lemail=request.form.get('email')
        lpw=request.form.get('pw')
        try :
            if lemail!='' and lpw!='':
                if  dc.check_pw(lpw) and dc.check_mail(lemail):
                    return redirect(f'/home/{dc.get_uname(lemail)}/')
                else:
                    return render_template('login.html', hidden='off' ,text='Email or password not registered')
            else:
                return render_template('login.html', hidden='off', text="Do not allow spaces. Please enter a value.")     
        except:
            return render_template('login.html', hidden='off', text="Login failed Please try again!")    

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
                    flash('Signup successful! Return to the login page :D')
                    return redirect('/login/')
                else:
                    return render_template('signup.html', hidden='off' ,text='Duplicate name or email. Please enter a different value.')
            else:
                return render_template('signup.html', hidden='off', text="Do not allow spaces. Please enter a value.")     
        except:
            return render_template('signup.html', hidden='off', text="Signup failed Please try again!")


# app.config['MAIL_SERVER'] = 'smtp.naver.com'
# app.config["MAIL_PORT"] = 465
# app.config['MAIL_USERNAME'] = ''
# app.config['MAIL_PASSWORD'] = ''
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

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
