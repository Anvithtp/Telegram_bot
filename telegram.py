ADAFRUIT_IO_USERNAME = "anvith_tp"
ADAFRUIT_IO_KEY = "aio_dyvz92BoMEP8LcDj7eUyEG0FleGN"

from Adafruit_IO import Client,Data
from telegram.ext import updater,CommandHandler

amn = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY) #client here is object

def on(bot,updater):
  chat_id = update.message.chat_id
  amn.create_data('telegram',Data(value=1))#telegram is the feed name
  bot.send_message(chat_id = chat_id,text = "LIGHT TO TURNED ON")
  
def off(bot,updater):
  chat_id = update.message.chat_id
  amn,create_data('telegram',Data(value=0))#telegram is the feed name
  bot.send_message(chat_id = chat_id,text = "LIGHT IS TURNED OFF")
  
updater = Updater('1565933627:AAEl4xDPOqVTwpP-dsSlgdRnKukndV1AW80')

dp = updater.dispatcher #updater is object and .dispatcher is attribute
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling()#updater is object and 
updater.idle()
