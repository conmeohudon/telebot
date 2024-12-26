import requests


def welcome(bot):
    def send_welcome(message):

        print(message.from_user.id)
        user_name = message.from_user.last_name
        bot.reply_to(message, f"Hello {user_name}, mời dùng hehe:\n"
                          f"/hello : Chao xìn\n"
                          f"/news : Đọc báo\n"
                          f"/cat : Ảnh mèo\n"
                          f"/cutegirl : Ảnh Diễm\n")
    return send_welcome
