# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:59:46 2021

@author: ALFA ELectronics
"""

from transliterate import to_cyrillic, to_latin
import telebot
from telebot import types

TOKEN = "5072241577:AAFKfC9McClYcB-x8NO_87NQ12GuC1LmYik"
bot = telebot.TeleBot(TOKEN, parse_mode=None)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu Alaykum Xush kelibsiz!"
    javob += "\nBy @nurbekdev"
    javob += "\nMatn kiring"
    bot.reply_to(message, javob)
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)
    


bot.polling()
