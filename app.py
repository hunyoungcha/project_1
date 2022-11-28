#home.html 디자인 고치기
#input time으로 받은 값 받아와서 if realtime==inputtime 하면 mail보내기
#database에 uname email pw 뒤에 wanttime 하나 하고
#기존에 데이터 가져오던것들은 다 [:2]로 고쳐서 받아오기



from flask import Flask, render_template, request, redirect, flash
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
        return render_template('home.html', name=uname, time=dc.get_data(uname,'uname','time'))
    elif request.method=='POST':
        try:
            time=request.form.get('time')
            dc.update_data('uname',uname,'time',time)
            flash("Saved successfully.")
            return redirect(f'/home/{uname}/')
        except:
            flash("An error has occurred.")
            return redirect('/')


@app.route('/delete/<uname>')
def delete(uname):
    try:
        if dc.delete_data(uname)==True:
            flash("Deleted successfully.")
            return redirect('/')
    except:
        flash('An error has occurred.')
        return redirect('/')




@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        try :
            lemail=request.form.get('email')
            lpw=request.form.get('pw')
            if lemail!='' and lpw!='':
                if  dc.check_data(lpw,'pw') and dc.check_data(lemail,'email'):
                    return redirect(f'/home/{dc.get_data(lemail,"email","uname")}/')
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
                if dc.check_data(suname,'uname')==False and dc.check_data(semail,'email')==False:
                    dc.add_data(suname,semail,spw)
                    flash('Signup successful! Return to the login page :D')
                    return redirect('/login/')
                else:
                    return render_template('signup.html', hidden='off' ,text='Duplicate name or email. Please enter a different value.')
            else:
                return render_template('signup.html', hidden='off', text="Do not allow spaces. Please enter a value.")     
        except:
            return render_template('signup.html', hidden='off', text="Signup failed Please try again!")





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
