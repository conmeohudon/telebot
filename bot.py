import telebot
import requests
import os
import random
from bs4 import BeautifulSoup

bot = telebot.TeleBot("7833971641:AAF6u72en5VjQa1vVCEoqresNEZp_NDEDCA", parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.reply_to(message, f"/hello : Chao xìn\n"
                          f"/news : Đọc báo\n"
                          f"/cat : Ảnh mèo\n"
                          f"/diem : Ảnh Diễm\n")

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    print(message)
    user_name = message.from_user.last_name
    bot.reply_to(message, f"Hello {user_name}")


@bot.message_handler(commands=['news'])
def getnew(message):
    request = requests.get("https://baomoi.com/tin-moi.epi")

    if request.status_code == 200:

        soup = BeautifulSoup(request.text, 'html.parser')

        baomoi = soup.find_all('h3', class_='font-semibold block')[:5]

        for baiviet in baomoi:
            title = baiviet.find('a')['title']
            link = baiviet.find('a')['href']
            bot.reply_to(message, f"Báo mới hôm nay\n"
                                  f"Tiêu đề: {title}\n"
                                  f"Link: https://baomoi.com{link}")
    else:
        print(f"Lỗi: {request.status_code}")


@bot.message_handler(commands=['cat'])
def send_cat(message):
    try:
        r = requests.get("https://api.thecatapi.com/v1/images/search")
        if r.status_code != 200:
            bot.reply_to(message, f" lỗi: {r.status_code}")
            return

        data = r.json()
        url = data[0].get("url")
        if not url:
            bot.reply_to(message, "Không tìm thấy ảnh.")
            return

        bot.send_photo(chat_id=message.chat.id, photo=url)
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {str(e)}")

# lmao
IMAGE_FOLDER = r"D:\ảnh lmao\Telegram Desktop"

@bot.message_handler(commands=['diem'])
def send_diem(message):
    try:
            all_files = os.listdir(IMAGE_FOLDER)
            image_files = [f for f in all_files if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            if not image_files:
                bot.reply_to(message, "Không tìm thấy ảnh trong thư mục.")
                return

            random_image = random.choice(image_files)
            random_image_path = os.path.join(IMAGE_FOLDER, random_image)

            with open(random_image_path, "rb") as photo:
                bot.send_photo(chat_id=message.chat.id, photo=photo)
    except Exception as e:
        bot.reply_to(message, f"Đã xảy ra lỗi: {str(e)}")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
