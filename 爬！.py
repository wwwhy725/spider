import requests 
from bs4 import BeautifulSoup
import json
import random
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
           'Host': 'movie.douban.com',
           'Referer': 'https://movie.douban.com/subject/1292052/'}
movie = []
result = []
counter = 0
#按字典形式输出
def dic_print(a1,a2,a3):
    info = {}
    a = '\n片名:' + a1 + a2 + '评分:' + a3
    t = a.strip().split('\n')
    for i in range(len(t)):
        flag = 0
        for j in range(len(t[i])):
            if t[i][j] != ':':
                flag = 0
            else:
                flag = 1
                break
        if flag == 1:
            if t[i].split(':',1)[1] == '':
                info[t[i].split(':',1)[0]] = t[i+1].split(':',1)[0]
            else:
                info[t[i].split(':',1)[0]] = t[i].split(':',1)[1]
        else:
            pass
        

    for elemen in info:
        info[elemen] = info[elemen].split('/')

    for el in info:
        if len(info[el]) == 1:
            info[el] = info[el][0]
    return info

#先爬取top250页面上所有电影的链接
for i in range(4):
    ori_url = 'https://movie.douban.com/top250?start={}&filter='.format(i*25)
    resp = requests.get(ori_url,headers = headers)
    soup = BeautifulSoup(resp.text,"html.parser")
    for k in soup.find_all('div',class_ = 'hd'):
        mov_site = k.find_all('a')
        print(mov_site)
        #movie.append(mov_site[0].get('href'))
#print(movie)
'''    
#movie里的url爬取具体信息
for url in movie:
    a_list = []
    res = requests.get(url,headers = headers)
    soup_ = BeautifulSoup(res.text,"html.parser")

    #随机睡几秒防止被认出
    time.sleep(random.randint(5,10))
    
    #电影名
    for tag in soup_.find_all(name = 'h1'):
        a_list.append(tag.find_all('span',{'property':'v:itemreviewed'})[0].text)
        
    #电影信息
    a_list.append(soup_.find_all('div',{'id':'info'})[0].text)
        
    #评分
    a_list.append(soup_.find_all('strong',{'class':'ll rating_num'})[0].text)
    
    a1 = a_list[0]
    a2 = a_list[1]
    a3 = a_list[2]
    result.append(dic_print(a1,a2,a3))
    counter += 1
    print('已成功爬取电影{}/100'.format(counter))
    
        
#写入json文件
with open('result.json','a',encoding = 'utf8') as f:
    json.dump(result,f,ensure_ascii = False)

'''


