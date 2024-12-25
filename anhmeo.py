import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.pinterest.com/search/pins/?rs=ac&len=2&q=%E1%BA%A3nh%20m%C3%A8o%20b%E1%BB%B1a&eq=%E1%BA%A3nh%20m%C3%A8o%20b%C6%B0a&etslf=1569")

if request.status_code == 200:

    soup = BeautifulSoup(request.text, 'html.parser')

    meo = soup.find_all('div', class_='vbI XiG')

    for anhmeo in meo:
        title = anhmeo.find('a')['title']
        link = anhmeo.find('a')['href']
        print(f"Title: {"Báo mới hôm nay"}")
        print(f"Title: {title}")
        print(f"Link: https://baomoi.com{link}")
else:
    print(f"Lỗi: {request.status_code}")