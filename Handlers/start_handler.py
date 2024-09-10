import telebot

def send_welcome(message, bot):
    bot.reply_to(message, "Hello, how are you doing?")