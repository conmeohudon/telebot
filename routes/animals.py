import requests


def handler_cat(bot):
    def send_cat(message):
        try:
            r = requests.get("https://api.thecatapi.com/v1/images/search")
            if r.status_code != 200:
                bot.reply_to(message, f" lỗi: {r.status_code}")
                return

            data = r.json()
            photo = data[0].get("url")
            if not photo:
                bot.reply_to(message, "Không tìm thấy ảnh.")
                return

            bot.send_photo(chat_id=message.chat.id, photo=photo)
        except Exception as e:
            bot.reply_to(message, "Lỗi mất ròi...")
            return

    return send_cat
