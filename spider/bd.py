import requests
import re
from multiprocessing import Process
import os
def get_img(html):
	r = r'"objURL":"(.+?)"'
	return re.findall(r,html,re.S)
def write(jpg):
	with open('Desktop\\baidu_img\\%s'%jpg[-5:],'wb') as f:
		try:
			img = requests.get(jpg,timeout=1)
			f.write(img.content)
			print('ok,%s'%jpg)
		except Exception as e:
			pass
def delet():
	if os.path.exists('Desktop\\baidu_img'):
		os.system('del Desktop\\baidu_img')
	else:
		os.system('mkdir Desktop\\baidu_img')
if __name__ == '__main__':
	delet()
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
	name = input("baidu_img_name:") 
	url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s'%name
	html = requests.get(url,headers=headers)
	html = html.text
	jpg_list = get_img(html)
	for jpg in jpg_list:
		pw = Process(target=write,args=(jpg,))
		pw.start()
	pw.join()