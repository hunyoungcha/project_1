#-*-coding:utf-8-*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html=urlopen("https://m.blog.naver.com/clearchem/221652792281")
obj=bs(html,"html.parser")

text_data=[]
for i in obj.select('.se-fs-' ):
    if i.get_text()!='\u200b':
        text_data.append(i.get_text())
print(text_data)

data=open('text_database.txt','w', encoding="UTF-8")
for i in range(len(text_data)):
    try:
        int(text_data[i+1].split(' ',1)[0].split('.')[0])
        data.write(text_data[i]+"\n")
    except:
        data.write(text_data[i])

data.close()