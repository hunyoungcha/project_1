#execpt 부분 alert로 실패 알림 하고 다시 render_template('/')


from flask import Flask, render_template, request, session, url_for, redirect
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


@app.route('/mail/', methods=['GET', 'POST'])
def mail():
    try:
        address=request.values.get('emailAddress')
        address=request.values.get('emailAddress')
        msg = Message('Hello', sender='chamgf5247@naver.com', recipients=[address])
        msg.body = 'Hello Flask message sent fro Flask-Mail'
        Mail(app).send(msg)
        return redirect('/')
    except:
        return redirect('/#signup')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
