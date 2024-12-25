import os
import random

import telebot

import config
from services.news import get_news
from routes.animals import handler_cat

bot = telebot.TeleBot(config.token_tele, parse_mode=None)


# @bot.message_handler(commands=['start'])
# def start(message):
#     print(message.from_user.id)
#     bot.reply_to(message, f"/hello : Chao xìn\n"
#                           f"/news : Đọc báo\n"
#                           f"/cat : Ảnh mèo\n"
#                           f"/diem : Ảnh Diễm\n")
#
#
# @bot.message_handler(commands=['hello'])
# def send_welcome(message):
#     print(message)
#     user_name = message.from_user.last_name
#     bot.reply_to(message, f"Hello {user_name}")
#
#
# @bot.message_handler(commands=['news'])
# def getnew(message):
#     get_news(bot=bot, message=message)
#
#
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

bot.register_message_handler(handler_cat(bot), commands=["cat"])


if "__main__" == __name__:
    bot.infinity_polling()
