import re
import urllib.request
import time
def getHTML(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
def getJPG(html,filename):
    r = r'src="(.+?\.jpg)" size'
    re_jpg=re.compile(r)
    html=html.decode('utf-8')
    JpgList=re.findall(re_jpg,html)
    for jpgurl in JpgList:
        urllib.request.urlretrieve(jpgurl,"Desktop\\tieba_img\\%s.jpg"%filename)
        print('file"%s.jpg"done'%filename)
        time.sleep(1.5)
        filename+=1
    return filename
url1=input('url:')
num = 0
while True:
    num +=1
    url = url1
    url = url+'?pn=%s'%num
    print(url)
    html=getHTML(url)
    if num == 1:
        filename = getJPG(html,0)
    else:
        filename = getJPG(html,filename)
'''
import os
def l(i):
    path = 'C:\\Users\\admin\\Desktop\\demo'
    print(path+'\\%s.jpg'%i)
    if os.path.exists(path+'\\%s.jpg'%i):
        os.system('del '+path+'\\%s.jpg'%i)
for i in range(0,200):
    l(i)
'''