import requests
from bs4 import BeautifulSoup

request = requests.get("https://baomoi.com/")

if request.status_code == 200:

    soup = BeautifulSoup(request.text, 'html.parser')

    baomoi = soup.find_all('h3', class_='font-semibold block')

    for baiviet in baomoi:
        title = baiviet.find('a')['title']
        link = baiviet.find('a')['href']
        print(f"Title: {"Báo mới hôm nay"}")
        print(f"Title: {title}")
        print(f"Link: https://baomoi.com{link}")
else:
    print(f"Lỗi: {request.status_code}")
