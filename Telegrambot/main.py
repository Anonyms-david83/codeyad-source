import time

import requests
import telebot
from telebot import types
import datetime

Token = '5851976531:AAEYO9_jd8MzXkDpK9omkLuvEm1FRwbz9Jg'
bot = telebot.TeleBot(Token)
url = "fhttps://api.binance.com/api/v3/ticker/price?symbol={symbol}"

updates = bot.get_updates()
for update in updates:
    chat_id = update.message.chat.id

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message.text)
    print(datetime.datetime)
    bot.reply_to(message, "به بات باباکبصی خوش اومدید (: این بات براتون عکسای باباکصبی رو میفرسته")
    image = open(r"D:\1650360530344.jpg", 'rb')
    bot.send_photo(chat_id, image)
    image.close()
    bot.send_message('دکمه زیر بابا رو وارد کنید تا سکه وارد شود')


markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton('💰')
markup.add(itembtn1)
bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    symbol = message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    data = response.json()
    if response.status_code == 200:
        print(response.status_code)
        print(data)
        bot.reply_to(message, f"{data['symbol']} price is {data['price']}")
    else:
        print(response.status_code)
        bot.reply_to(message,"there is something wrong with your crypto symbol")


while True :
    try:
     bot.polling()
    except Exception :
        time.sleep(15)

