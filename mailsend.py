import datacon as dc
from flask_mail import Mail, Message
from flask import Flask
import time

#idle로 따로 돌릴거
#vscode로 웹 띄우고 이파일은 idle로 백그라운드 서버 처럼 사용할것

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.naver.com'
app.config["MAIL_PORT"] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



# while True:
#     db=dc.pret()
#     for i in range(len(db)):
#         if db[i]['time']==f'{time.localtime().tm_hour}:{time.localtime().tm_min}':
#             msg = Message('Hello', sender='chamgf5247@naver.com', recipients=db[i]['email'])
#             msg.body = 'Hello Flask message sent fro Flask-Mail'
#             Mail(app).send(msg)
#     print("---실행중---")
#     time.sleep(50)
    
db=dc.pret()
for i in range(len(db)):
    # if db[i]['time']==f'{time.localtime().tm_hour}:{time.localtime().tm_min}':
    msg = Message('Hello', sender='chamgf5247@naver.com', recipients=db[i]['email'])#오류 나는거 고쳐야 함
    msg.body = 'Hello Flask message sent fro Flask-Mail'
    Mail(app).send(msg)
