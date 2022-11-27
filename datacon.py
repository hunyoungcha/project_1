def pret():   #데이터 전처리 (txt파일에 있는 데이터 읽어와서 2중 배열로 만듬)
    data=open('database.txt','r')
    dline=data.readlines()
    dline=list(map(lambda s : s.strip(), dline))
    dline=list(filter(None, dline))
    database=[]
    for i in range(len(dline)):
        database.append(dline[i].split())
    data.close()
    return database


def delete_data(uname):    #데이터 삭제 (리스트에서 조건 맞는거 삭제 시킨후 리스트 그대로 다시 txt 파일에 재생성)
    data=pret()
    is_name=0
    for i in range(len(data)):
        if uname==data[i][0]:
            is_name=1
            del data[i]
            
    if is_name==0:
        return False

    rem_data=open('database.txt','w')
    for j in range(len(data)):
        for k in range(3):
            rem_data.write(f'{data[j][k]} ')
        if len(data)-j!=1:
            rem_data.write('\n')
        else:
            rem_data.close()
    return rem_data


def add_data(uname,email,pw):   #데이터 추가 (회원가입 기능, txt파일 맨 밑줄에 정보가 적힘)
    data=open('database.txt', 'a')
    data.write(f'\n{uname} {email} {pw}')
    data.close()


def add_time(uname,time):
    



#################################################################
def check_uname(name):
    data=pret()
    for i in range(len(data)):
        if name==data[i][0]:
            return True
    return False

def check_mail(mail):
    data=pret()
    for i in range(len(data)):
        if mail==data[i][1]:
            return True
    return False

def check_pw(pw):
    data=pret()
    for i in range(len(data)):
        if pw==data[i][2]:
            return True
    return False

def get_uname(mail):
    data=pret()
    for i in range(len(data)):
        if mail==data[i][1]:
            return data[i][0]
    return False


#################################################################
