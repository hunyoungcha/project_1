#-*-coding:utf-8-*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html=urlopen("https://m.blog.naver.com/clearchem/221652792281")
obj=bs(html,"html.parser")

data=open('text_database.txt','w', encoding="UTF-8")
for i in obj.select('.se-fs-' ):
    if i.get_text()!='\u200b':
        if i.get_text().split(' ',1)[0].split('.')[0]!=type  #숫자로 시작 안할경우 앞에 문자 열 readlines로 불러와서 제일 마지막거만 변수에 저장한 후 +해서 변수에 저장하고 그걸 write하기 
        data.write(i.get_text()+'\n')
data.close()