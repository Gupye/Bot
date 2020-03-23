import time
import telebot
from telebot import types
import threading

from XMLpars import xmlpars

bot = telebot.TeleBot('1048945938:AAHX_0SBJJhwaXkzj-n7OxlFlsxaK6vvFHU', threaded=True)  # Инициализация бота
menu_markup = 'markup_report'
markup_start = types.ReplyKeyboardMarkup(row_width=2)
markup_start.add('Привет')
markup_start.add('Отчёт')
markup_start.add('Пока')


@bot.message_handler(commands=['start'])  # Вывод первого меню по команде \start
def start_message(message):
    global markup_start, menu_markup
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup_start)
    menu_markup = 'markup_start'


@bot.message_handler(content_types=['text'])  # Начало хендлера
def send_text(message):
    global menu_markup
    print(message.from_user.username, 'в чате', message.chat.title, message.chat.id, 'написал',
          # мониторинг сообщений от пользователей
          message.text.lower())
    if message.text.lower() == 'тест':
        a = message.chat.id
        bot.send_message(message.chat.id, a)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Дороу')
    elif message.text.lower() == 'меня зовут маргарита':
        bot.send_message(message.chat.id, 'Ты самая лучшая жена')
    elif message.text.lower() == 'создатель':
        bot.send_message(message.chat.id, 'Gupye, vk.com/gupye, +79788781055')
    elif message.text.lower() == 'отчёт->сформировать':
        xmlpars()
        bot.send_message(message.chat.id, 'Отчёт сформирован')
    elif message.text.lower() == 'назад->':  # Вывод меню для получения отчёта
        if menu_markup == 'markup_report':
            bot.send_message(message.chat.id, 'назад ', reply_markup=markup_start)
        elif menu_markup == 'markup_start':
            bot.send_message(message.chat.id, 'это уже верхний уровень')
    elif message.text.lower() == 'отчёт':  # Вывод меню для получения отчёта
        markup_report = types.ReplyKeyboardMarkup(row_width=2)
        markup_report.add('Отчёт->операции')
        markup_report.add('Отчёт->скидки')
        markup_report.add('Отчёт->сформировать')
        markup_report.add('Назад->')
        bot.send_message(message.chat.id, 'выберите тип отчёта', reply_markup=markup_report)
        menu_markup = 'markup_report'
    elif message.text.lower() == 'отчёт->скидки' or message.text.lower() == 'отчет->скидки':  # Вывод отчёта по скидкам
        f = open('Скидки.txt', 'r', encoding="utf-8")
        a = f.read()
        if len(a)!=0:
            bot.send_message(message.chat.id, a)
        else:
            bot.send_message(message.chat.id, 'Отчёт пуст')
        f.close()
    elif message.text.lower() == 'отчёт->операции' or message.text.lower() == 'отчет->операции':  # Вывод отчёта по операциям
        f = open('Операции.txt', 'r', encoding="utf-8")
        a = f.read()
        if len(a) != 0:
            bot.send_message(message.chat.id, a)
        else:
            bot.send_message(message.chat.id, 'Отчёт пуст')
        f.close()


def sendler():
    while True:
        try:
            print('запуск парсера')
            xmlpars()
            time.sleep(900)
        except Exception as e:
            print(e)
        time.sleep(15)


def polling():
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
    time.sleep(15)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = str(message.document.file_name)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
        bot.reply_to(message, e)


p2 = threading.Thread(target=polling, args=())
p1 = threading.Thread(target=sendler, args=())
p2.start()
p1.start()
p2.join()
p1.join()
