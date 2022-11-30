# project_1 
하루 한번 원하는 시간에 명언을 메일로 보내주는 웹 사이트 입니다.

app.py로 웹사이트를 돌리고 bg_server로 메일을 보냅니다.

datacon.py로 data를 관리하고 서버로 넘어 오기전 데이터 전처리를 합니다

db는 txt파일로 관리했고 모든 데이터는 txt -> datacon.py -> server 순으로 갑니다.

txt파일의 데이터들을 datacon.py에서 uname, email, pw, time의 키값으로 딕셔너리를 만들어 전처리 했습니다.
