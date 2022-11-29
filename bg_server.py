#idle로 따로 돌릴거
#vscode로 웹 띄우고 이파일은 idle로 백그라운드 서버 처럼 사용할것
import smtplib
from email.mime.text import MIMEText
import datacon as dc
import time



while True:
    db=dc.pret()
    for i in range(len(db)):
        if db[i]['time']==f"{time.localtime().tm_hour}:{time.strftime('%M', time.localtime())}": 
            smtp = smtplib.SMTP('smtp.naver.com', 587)
            smtp.ehlo()      # say Hello
            smtp.starttls()  # TLS 사용시 필요
            smtp.login('', '') #아이디 비번 넣기
            msg = MIMEText('151232')
            msg['From'] ='chamgf5247@naver.com'
            msg['Subject'] = 'test123'
            msg['To'] =f"{db[i]['email']}"
            smtp.sendmail('chamgf5247@naver.com', f"{db[i]['email']}", msg.as_string())
            print('send mail to',db[i]['email'])
    print(f"---실행중--- {time.localtime().tm_hour}:{time.strftime('%M', time.localtime())}")
    time.sleep(60)
    

