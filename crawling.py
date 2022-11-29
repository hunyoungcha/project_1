#-*-coding:utf-8-*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html=urlopen("https://m.blog.naver.com/clearchem/221652792281")
obj=bs(html,"html.parser")

data=open('text_database.txt','w', encoding="UTF-8")
for i in obj.select('.se-fs-' ):
    #크롤링 해서 db넣기 전에 한줄 띄어쓰기 제거하고 넣는 법 알아내기
    data.write(i.get_text()+'\n')
data.close() 