import telebot
from config import TOKEN
from handlers import setup_handlers
from logger import Logger
from date import setup_date_handler

bot = telebot.TeleBot(TOKEN)
logger = Logger()

setup_handlers(bot, logger)
setup_date_handler(bot, logger) 

bot.polling()
