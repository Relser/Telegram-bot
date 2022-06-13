import config
import telebot
from pycbrf import ExchangeRates
from datetime import date
today = date.today()
rates = ExchangeRates(today)
bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "Привет! Просто напиши /help и сам всё узнаешь")
@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, "Я могу подсчитать курс валют:просто напиши команды /usd,/eur,/pln,/czk,/chf,/try")

@bot.message_handler(commands=["usd"])
def usd(message):
	text = '1 Доллар США '+ str(rates['USD'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["czk"])
def usd(message):
	text = '1 Чешская Крона '+ str(rates['CZK'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["chf"])
def usd(message):
	text = '1 Швейцарский франк '+ str(rates['CHF'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["try"])
def usd(message):
	text = '1 Турецкая Лира '+ str(rates['TRY'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["eur"])
def usd(message):
	text = '1 Евро '+ str(rates['EUR'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["pln"])
def pln(message):
	text = '1 Польский Золотой '+ str(rates['PLN'].rate)+ 'руб.'
	bot.send_message(message.chat.id, text)


if __name__ == '__main__':
	bot.infinity_polling()