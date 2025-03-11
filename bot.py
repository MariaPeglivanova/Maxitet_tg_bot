import telebot
from config import TOKEN
from handlers import setup_handlers
from logger import Logger

bot = telebot.TeleBot(TOKEN)
logger = Logger()

setup_handlers(bot, logger)

bot.polling()
