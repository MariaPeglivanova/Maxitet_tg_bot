import datetime 
import telebot 
 
def setup_date_handler(bot, logger): 
    @bot.message_handler(commands=['date']) 
    def send_date(message): 
        logger.log(message.chat.id, "/date") 
        today = datetime.date.today() 
        bot.send_message(message.chat.id, f"Сегодня: {today.strftime('%d-%m%Y')}")