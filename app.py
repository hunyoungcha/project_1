#메일 오류 나는거 고쳐야 함


from flask import Flask, render_template, request, session, url_for, redirect
from flask_mail import Mail, Message


app = Flask(__name__)



app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config['MAIL_USERNAME'] = 'hunyoung52472@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/mail/', methods=['GET', 'POST'])
def mail():
    address=request.values.get('emailAddress')
    msg = Message('Hello', sender='hunyoung5247@gmail.com', recipients=[address])
    msg.body = 'Hello Flask message sent fro Flask-Mail'
    Mail(app).send(msg)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
