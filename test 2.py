from telebot import types
from telebot import types
import telebot
bot = telebot.TeleBot('1048945938:AAHX_0SBJJhwaXkzj-n7OxlFlsxaK6vvFHU')
# Using the ReplyKeyboardMarkup class
# It's constructor can take the following optional arguments:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)
# row_width is used in combination with the add() function.
# It defines how many buttons are fit on each row before continuing on the next row.
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)
bot.send_message(445120756, "", reply_markup=markup)

