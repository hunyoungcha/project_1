#폼 데이터를 submit 하면 웹페이지 못찾고 있음 <== 해결해야함
#로그인 구현 되면 임시 디비 만들어서 거기에 저장해둘것
#로그인 성공 실패 페이지 만들어서 성공하면 홈페이지, 실패하면 다시 시도


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    id=request.form.get('id')
    pw=request.form.get('pw')
    return id, pw


app.run()