import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
           'Host': 'www.bu.edu',
           'Referer': 'https://www.bu.edu/stat/'}
homepage = []

url = 'https://www.bu.edu/stat/people/faculty/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
for k in soup.find_all('p'):  # 'div', class_=''
    if len(k.find_all('a')) == 0:
        continue
    else:
        per_home = k.find_all('a')
    homepage.append(per_home[0].get('href'))
  #print(homepage)

f = open("boston_sta.txt", "w")
for line in homepage:
    if 'http' in line:
        f.write(line+'\n')
    else:
        f.write('https://www.bu.edu/stat/people/faculty/'+line+'\n')
f.close()

