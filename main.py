import time
import telebot
from telebot import types
import threading

bot = telebot.TeleBot('1048945938:AAHX_0SBJJhwaXkzj-n7OxlFlsxaK6vvFHU', threaded=True)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add('Привет')
    markup.add('Отчёт')
    markup.add('Пока')
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global onwork
    print(message.from_user.username, 'в чате', message.chat.title, message.chat.id, 'написал',
          message.text.lower())
    if message.text.lower() == 'тест':
        a = message.chat.id
        bot.send_message(message.chat.id, a)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Дороу')
    elif message.text.lower() == 'меня зовут маргарита':
        bot.send_message(message.chat.id, 'Ты самая лучшая жена')
    elif message.text.lower() == 'иди нахуй' or message.text.lower() == 'пошёл нахуй' or message.text.lower() == 'пошел нахуй':
        bot.send_message(message.chat.id, 'Сам иди, урод.')
    elif message.text.lower() == 'создатель':
        bot.send_message(message.chat.id, 'Gupye, vk.com/gupye, +79788781055')
    elif message.text.lower() == 'отчёт->скидки' or message.text.lower() == 'отчет->скидки':
        f = open('Скидки.txt', 'r', encoding="utf-8")
        a = f.read()
        bot.send_message(message.chat.id, a)
        f.close()
    elif message.text.lower() == 'отчёт->операции' or message.text.lower() == 'отчет->операции':
        f = open('Операции.txt', 'r', encoding="utf-8")
        a = f.read()
        bot.send_message(message.chat.id, a)
        f.close()
    elif message.text.lower() == 'пришёл':
        if not onwork:
            onwork = True
            bot.send_message(message.chat.id, 'Зарегистрирован на работе')
        else:
            bot.send_message(message.chat.id, 'Ты уже на работе')
    elif message.text.lower() == 'ушёл':
        if onwork:
            onwork = False
            bot.send_message(message.chat.id, 'Пока, удачно отдохнуть')
        else:
            bot.send_message(message.chat.id, 'Ты не зарегался')


def sendler():
    while True:
        try:
            print('отправить сообщение')
            bot.send_message(445120756, 'каждые три секунды')
            time.sleep(15)
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
