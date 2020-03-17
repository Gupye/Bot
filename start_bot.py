import telebot
from telebot import apihelper


def start():
    PROXY = 'socks4://vpn.ugits.org:10090'
    apihelper.proxy = {'https': PROXY}
    bot = telebot.TeleBot('1048945938:AAHX_0SBJJhwaXkzj-n7OxlFlsxaK6vvFHU')
    return bot
