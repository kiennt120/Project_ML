list=['so-hoa','oto-xe-may','doi-song','du-lich','giai-tri','giao-duc','khoa-hoc','kinh-doanh','phap-luat','suc-khoe','the-thao','thoi-su']
import requests
from bs4 import BeautifulSoup
link_lisk=[]
for one in list:
    tmp=("https://vnexpress.net/") + one
    link_lisk.append(tmp)
for one in range(1,301):
    item=tmp+str(one)
    link_lisk.append(item)
for tmp1 in list:
    check=0
    dem=0
    data=[]
    links=[]
    for tmp2 in range(1,500):
        tmp3= ("https://vnexpress.net/") + tmp1+ '-p' + str(tmp2)
        response=requests.get(tmp3)
        soup = BeautifulSoup(response.content, "html.parser")
        if soup.findAll('h3', class_='title-news') is not None:
            titles = soup.findAll('h3', class_='title-news')
        else :
            if soup.findAll('h2', class_='title-news') is not None:
                titles = soup.findAll('h2', class_='title-news')
            else :
                titles = soup.findAll('h1', class_='title-news')
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
                print(title1.text)
                dem=dem+1
            else:
                continue
        if check==1:
            print(dem)
            break
    path_w='data/datatest/' + tmp1 +'.txt'
    print(path_w)
    with open(path_w, mode='w',encoding = "utf-8") as f:
        for text in data:
            f.write(text + '\n')
    f.close()





