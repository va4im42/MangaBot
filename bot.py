import telebot
from Handlers import start_handler, message_handler
from Services import backend_services
from Class import Manga

bot = telebot.TeleBot(token="6997181118:AAFbufT-1n5dwTUXT0dut3axYkNWZ5duPM8", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    start_handler.send_welcome(message, bot)

@bot.message_handler(commands=['search'])
def search(message):
    message_handler.search(message, bot)
    @bot.message_handler(func=lambda message: True)
    def mangalist(message):
        answers = backend_services.mangalist(message.text)
        for answer in answers:
            bot.reply_to(message,f"Name: {answer.name}, Сылка: {answer.link}, Pic: {answer.img}")

bot.infinity_polling()