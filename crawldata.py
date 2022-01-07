list=['so-hoa-p','thoi-su-p','oto-xe-may-p','doi-song-p','du-lich-p','giai-tri-p','giao-duc-p','khoa-hoc-p','kinh-doanh-p','phap-luat-p','suc-khoe-p','the-thao-p','thoi-su-p']
import requests
from bs4 import BeautifulSoup
list1='so-hoa'
tmp=("https://vnexpress.net/") + list1+ '-p'
link_lisk=[]
data=[]
for one in range(1,301):
    item=tmp+str(one)
    link_lisk.append(item)
dem=0
check=0
for one in link_lisk:
    response=requests.get(one)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll('h2', class_='title-news')
    links = [link.find('a').attrs["href"] for link in titles]
    for link in links:
        news = requests.get(link)
        soup = BeautifulSoup(news.content, "html.parser")
        title1 = soup.find("h1", class_="title-detail")
        if dem==2000:
            check=1
            break;
        if title1 is not None:
            data.append(title1.text)
            dem=dem+1
        else:
            continue
    if check==1:
        print(dem)
        break
path_w='data/' + list1 +'.txt'
print(path_w)
with open(path_w, mode='w',encoding = "utf-8") as f:
    for text in data:
        f.write(text + '\n')
f.close()





