import requests
from bs4 import BeautifulSoup


def handler_news(bot):
    def send_news(message):
        request = requests.get("https://baomoi.com/tin-moi.epi")
        if request.status_code == 200:

            soup = BeautifulSoup(request.text, 'html.parser')

            baomoi = soup.find_all('h3', class_='font-semibold block')[:5]

            title = [baiviet.find('a')['title'] for baiviet in baomoi]
            link = [baiviet.find('a')['href'] for baiviet in baomoi]

            text_content = ""

            for content in range(len(title)):
                text_content += f"Tiêu đề: {title[content]} \n Link:  https://baomoi.com/{link[content]} \n --------------------------------------- \n"

            bot.send_message(message.from_user.id, text_content)
        else:
            print(f"Lỗi: {request.status_code}")

    return send_news