def pret():
    #데이터 전처리 (txt파일에 있는 데이터 읽어와서 딕셔너리로 만듬)
    data=open('user_database.txt','r')
    dline=data.readlines()
    dline=list(map(lambda s : s.strip(), dline))
    dline=list(filter(None, dline))
    data.close()

    dic_name="uname", "email", "pw", "time"
    database=[]
    for i in range(len(dline)):
        count=0
        dic_maker={}
        for j in dic_name: 
            dic_maker[j]=dline[i].split()[count]
            count+=1
        database.append(dic_maker)
    return database

def delete_data(uname):
    db=pret()
    try:
        for i in range(len(db)):
            if db[i]['uname']==uname:
                del db[i]
                data_remake(db)
                return True
    except:
        return False

def add_data(uname,email,pw):   #데이터 추가 (회원가입 기능, txt파일 맨 밑줄에 정보가 적힘)
    data=open('user_database.txt', 'a')
    data.write(f'\n{uname} {email} {pw} 08:00')
    data.close()


def update_data(to_desc,to_data,from_desc,from_data): #to_desc이 to_data인 데이터의 from_desc를 from_data로 바꿔줘
    db=pret()                                           # ex) uname이 cha인 데이터의 time을 09:00로 바꿔줘
    for i in range(len(db)):
        if db[i][to_desc]==to_data:
            db[i][from_desc]=from_data
            data_remake(db)
            return True
    return False



##################################################################################################################################
def check_data(thing,desc): #thing은 데이터 칸: cha, who... desc는 설명칸: uname, email..
    db=pret()
    for i in db:
        if thing==i[desc]:
            return True
    return False

def get_data(thing,desc,get): #thing= data, desc를 통해 가져올거, get은 가져올 데이터
    db=pret()
    for i in db:   #cha uname email <=data는 cha고 uname을 통해 email가져올거
        if thing==i[desc]:
            return i[get]
    return None

def data_remake(changed_db):   #특정 상황에서 db가 영구적으로 바껴야 하는 경우, 바뀐 db를 파라미터로 넣으면 됨
    data=open('user_database.txt', 'w')
    for i in range(len(changed_db)):
        for j in "uname", "email", "pw", "time":
            data.write(f'{changed_db[i][j]} ')
        if len(changed_db)-i!=1:
            data.write('\n')
##################################################################################################################################




def text_get(num):
    data=open('text_database.txt','r', encoding='utf-8')
    dline=data.readlines()
    return dline[num].split(' ',1)[1].split('\n')[0]


