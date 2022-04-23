import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import datetime

today_ = date.today()

# dd/mm/YY
today = str(today_.day) + "/" + str(today_.month) + "/" + str(today_.year)
today = datetime.datetime.strptime(today, '%d/%m/%Y')

data_dir = "./input/"
last_month = date(today_.year, today_.month - 2, today_.day)
delta = today_ - last_month
index = 0
for i in range(delta.days + 1):
    day = last_month + timedelta(days=i)
    day = str(day.day) + "-" + str(day.month) + "-" + str(day.year)
    url = "https://tuoitre.vn/xem-theo-ngay/" + day + ".htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    titles = soup.findAll('h3', class_='title-news')
    links = [link.find('a').attrs["href"] for link in titles]
    for link in links:
        news = requests.get("https://tuoitre.vn" + link)
        soup = BeautifulSoup(news.content, "html.parser")
        try:
            title = soup.find("h1", class_="article-title").text
            abstract = soup.find("h2", class_="sapo").text
            body = soup.find("div", id="main-detail-body")
            paras = body.findChildren("p", recursive=False)
            content = ""
            for p in paras:
                content += p.text
            with open(data_dir + str(index) + '.txt', 'w', encoding='utf-8') as f:
                f.write(content)
                index += 1
            # print("Tiêu đề: " + title)
            # print("Mô tả: " + abstract)
            # print("Nội dung: " + content)
            # print("_________________________________________________________________________")
        except:
            continue
