import os
import random

def diem(bot):
    def send_diem(message):
            try:
                folder = r"D:\ảnh lmao\Telegram Desktop"
                file = os.listdir(folder)

                image = [f for f in file if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

                if not file:
                    bot.reply_to(message, "Không tìm thấy ảnh trong thư mục.")
                    return

                random_image = random.choice(image)
                random_image_path = os.path.join(folder, random_image)

                with open(random_image_path, "rb") as photo:
                    bot.send_photo(chat_id=message.chat.id, photo=photo)
            except Exception as e:
                bot.reply_to(message, "Lỗi rồi em ơi")

    return send_diem
