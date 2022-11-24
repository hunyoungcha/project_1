

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
    for i in range(len(data)):
        if uname==data[i][0]:
            del data[i]

    rem_data=open('database.txt','w')
    for j in range(len(data)):
        for k in range(3):
            rem_data.write(f'{data[j][k]} ')
        if len(data)-j!=1:
            rem_data.write('\n')
        else:
            rem_data.close()
    return rem_data


def update_data(uname,email,pw):   #데이터 추가 (회원가입 기능, txt파일 맨 밑줄에 정보가 적힘)
    data=open('database.txt', 'a')
    data.write(f'\n{uname} {email} {pw}')
    data.close()
    return data

#메일 중복 체크하는 함수 만들기
#만들고 나면 update, delete 하기 전에 체크 하고 들어가기 
#체크해서 중복되면 retrun flase하기
#app.py에선 try execpt 해서 flase 받으면 실패 페이지 보내기