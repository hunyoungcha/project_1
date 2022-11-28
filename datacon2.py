class pret:
    #데이터 전처리 (txt파일에 있는 데이터 읽어와서 딕셔너리로 만듬)
    data=open('database.txt','r')
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
print(pret.database)

#이중 배열 => 딕셔너리로 바꿨음
#crud 다시 만들고 함수 부르는거 다시 다 바꿔주기
#