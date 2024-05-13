

import os
import requests
from bs4 import BeautifulSoup as bs

from telebot import TeleBot,telebot,types
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton

bot = telebot.TeleBot(os.getenv('imgBotToken'))

button = InlineKeyboardMarkup()
group = InlineKeyboardButton(text='⚡️Our Group⚡️',url='t.me/developerschat')
channel = InlineKeyboardButton(text='⚡️Our Channel⚡️',url='t.me/developerspage')
button.add(group,channel)

@bot.message_handler(commands=['start'])
def welcome_message(msg):
    user = msg.from_user
    id = msg.from_user.id
    name = user.first_name
    first_name = f"<a href='tg://user?id={id}'>{name}</a>"
    text = f'''Hello {first_name} welcome to image downloader bot😊

ሠላም ውድ {first_name} እንኳን ወደ ፎቶ ማውረጃ ቦት በሠላም መጡ😊'''
    bot.send_message(msg.chat.id,text,reply_markup=button,parse_mode='HTML')

@bot.message_handler(commands=['help'])
def help(message):
    text = '''አጠቃቀም
የፈለጋችሁትን ፎቶ ፅፋቹ ላኩለት፤ለምሳሌ Cat ከዛ ቦቱ ፎቶውን አውርዶ ይልክላችሗል።

How to use?
It's pretty eas using this bot. Just send me a name of photo you wanna download.

Example Cat
The bot immediately download the image then sends to you.'''
    bot.reply_to(message,text)
    
@bot.message_handler(func=lambda m: True)
def image_downloader(msg):
    text = msg.text
    url = 'https://unsplash.com/s/photos/' + text
    header = { 'User-Agent': 'Generic user agent' }
    request = requests.get(url,headers = header)
    soup = bs(request.text,'html.parser')
    imgs = soup.select('div img')
    image = imgs[0]['src']
    image2 = imgs[1]['src']
    bot.send_photo(msg.chat.id,image,reply_to_message_id=msg.message_id)
    bot.send_photo(msg.chat.id,image2,reply_markup=button)
bot.infinity_polling()
