#메일 오류 나는거 고쳐야 함


from flask import Flask, render_template, request, session, url_for, redirect
import os
from flask_mail import Mail, Message

app = Flask(__name__)
mail=Mail()


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hunyoung5247@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/mail/')
def mail():
    msg = Message('Hello', sender='hunyoung5247@gmail.com', recipients=['chamgf5247@naver.com'])
    msg.body = 'Hello Flask message sent fro Flask-Mail'
    mail.send(msg)
    return 'Sent'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
