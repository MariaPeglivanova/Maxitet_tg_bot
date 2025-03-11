import datetime
import telebot

def setup_handlers(bot, logger):
    @bot.message_handler(commands=['start'])
    def start(message):
        logger.log(message.chat.id, "/start")
        bot.send_message(message.chat.id, "Привет! Я бот.")

    @bot.message_handler(commands=['help'])
    def help(message):
        logger.log(message.chat.id, "/help")
        bot.send_message(message.chat.id, "Я умею показывать время. Введите /time.")

    @bot.message_handler(commands=['time'])
    def send_time(message):
        logger.log(message.chat.id, "/time")
        now = datetime.datetime.now()
        bot.send_message(message.chat.id, f"Текущее время: {now.strftime('%H:%M:%S')}")
