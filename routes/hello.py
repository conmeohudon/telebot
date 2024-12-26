def send_hello(bot):
    def hello(message):
        print(message)
        user_name = message.from_user.last_name
        bot.reply_to(message, f"Hello {user_name}")
    return hello