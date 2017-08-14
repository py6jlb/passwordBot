"""
Routes and views for the flask application.
"""

from flask import request, abort
from . import mybot
from .. import db
from ..models import Adjectives, Adverbs, Nouns, Verbs
from  sqlalchemy.sql.expression import func, select
import random
from .Translit import Translit
from .EntropyCalc import EntropyCalc

import telebot
import logging

TOKEN = '#TOKEN'
sequence_delimetr = ['_', '-', '+', '=']
sequence_framed = ['!', '#', '@', '$', '%', '*', '?']

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
file_output_handler = logging.FileHandler('log.txt')
file_output_handler.setFormatter(telebot.formatter)
telebot.logger.addHandler(file_output_handler)

bot = telebot.TeleBot(TOKEN, threaded=False)
tr = Translit()
entrop = EntropyCalc()

@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Get my password')
    bot.send_message(message.from_user.id, 'Select actions:', reply_markup=user_markup)


@bot.message_handler(func=lambda mess: "Get my password" == mess.text, content_types=['text'])
def handle_text(message):
    result = ''
    words = []
    framed_symbol = ''
    
    delimeter= random.choice(sequence_delimetr)
    framed = random.choice([True, False])
    if framed:
        framed_symbol = random.choice(sequence_framed)
    words.append(Verbs.query.order_by(func.random()).first().word)
    words.append(Adverbs.query.order_by(func.random()).first().word)
    words.append(Adjectives.query.order_by(func.random()).first().word)
    words.append(Nouns.query.order_by(func.random()).first().word)
    
    result += framed_symbol
    while len(words) > 0:
        selected_word = random.choice(words)
        result += str(selected_word)
        if len(words) > 1:
            result += delimeter
        words.remove(selected_word)
    result += framed_symbol

    result = tr.transliterate(result)
    entropy = entrop.calc(result)    
    bot.send_message(message.chat.id, 'Password: {0}, entropy: {1}bit'.format(result, entropy))

#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def echo_message(message):
#    bot.reply_to(message, message.text)


@mybot.route('/', methods=['GET', 'HEAD'])
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url="#URL")
    return "CONNECTED", 200


@mybot.route('/telegram', methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200

