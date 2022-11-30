import email.message
import smtplib




msg = email.message.Message()
msg['Subject'] = 'foo'
msg['From'] = 'chamgf5247@naver.com'
msg['To'] = 'hunyoung5247@gmail.com'
msg.add_header('Content-Type','text/html')
msg.set_payload(html)

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.naver.com',587)
s.ehlo()
s.starttls()
s.login('chamgf5247','Navergnsdud6361@')
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()