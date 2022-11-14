import random
import telebot
from telebot import types

bot = telebot.TeleBot('5588685007:AAEdXrvA9TzEwdtOPIdFavKq7U6EmZkDieQ')
keyboard = telebot.types.InlineKeyboardMarkup()

keyboard.row(       telebot.types.InlineKeyboardButton(text=' ', callback_data='no'),
                    telebot.types.InlineKeyboardButton(text='c', callback_data='C'),
                    telebot.types.InlineKeyboardButton(text='<=', callback_data='<='),
                    telebot.types.InlineKeyboardButton(text='/', callback_data='/') ) 

keyboard.row(       telebot.types.InlineKeyboardButton(text='7', callback_data='7'),
                    telebot.types.InlineKeyboardButton(text='8', callback_data='8'),
                    telebot.types.InlineKeyboardButton(text='9', callback_data='9'),
                    telebot.types.InlineKeyboardButton(text='*', callback_data='*') )

keyboard.row(       telebot.types.InlineKeyboardButton(text='4', callback_data='4'),
                    telebot.types.InlineKeyboardButton(text='5', callback_data='5'),
                    telebot.types.InlineKeyboardButton(text='6', callback_data='6'),
                    telebot.types.InlineKeyboardButton(text='-', callback_data='-') )

keyboard.row(       telebot.types.InlineKeyboardButton(text='1', callback_data='1'),
                    telebot.types.InlineKeyboardButton(text='2', callback_data='2'),
                    telebot.types.InlineKeyboardButton(text='3', callback_data='3'),
                    telebot.types.InlineKeyboardButton(text='+', callback_data='+') )

keyboard.row(       telebot.types.InlineKeyboardButton(text='', callback_data='no'),
                    telebot.types.InlineKeyboardButton(text='0', callback_data='C'),
                    telebot.types.InlineKeyboardButton(text=',', callback_data=','),
                    telebot.types.InlineKeyboardButton(text='=', callback_data='=') )                   
value = ''
old_value = ''
@bot.message_handler(commands=['start', 'calculater'])
def messages(message):
    global value
    if value == "":
      bot.send_message(message.from_user.id, '0', reply_markup = keyboard,)
    else:
       bot.send_message(message.from_user.id, value, reply_markup = keyboard,)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
         value[: len(value) - 1]
        try:
            value = str( eval(value))
        except:
            value = 'Ошибка!'
    else:
        value += data
    
    if ( value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup = keyboard )
            old_value =''
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup = keyboard )
            old_value = value

    if value == 'Ошибка!': value = ''
    
bot.polling(none_stop=True, interval=0)