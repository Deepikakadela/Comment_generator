
import requests
from bs4 import BeautifulSoup as bs
import os

def get(page):
    url = "https://github.com/search?p="+str(page)+"&q=java&type=Repositories&utf8=%E2%9C%93"
    soup = bs(requests.get(url).text)
    l = soup.find_all("a")
    new_l = []
    for i in l :
        if "v-align-middle" in str(i):
            new_l.append(str(i))
    urls = []
    for i in new_l:
        t = str(i).split("url")[1].split("}")[0][3:-1]
        urls.append(t)
    for i in urls:
        os.system("git clone "+ i+".git" )

for i in range(1,101):
    get(i)
