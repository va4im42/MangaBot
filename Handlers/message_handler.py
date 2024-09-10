import telebot
from Services import backend_services

def search(message, bot):
     bot.reply_to(message, "Что ты хочешь найти?")

def mangalist(message, bot):
     answer = backend_services.mangalist(message.text)
     bot.reply_to(message,answer)
    



