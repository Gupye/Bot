from time import sleep
import start_bot

onwork = False
wait = 15

# bot = telebot.TeleBot('1048945938:AAHX_0SBJJhwaXkzj-n7OxlFlsxaK6vvFHU')

bot = start_bot.start()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(commands=['test'])
def send_text1(message):
    global wait
    while True:
        bot.send_message(message.chat.id, 'каждые три секунды')
        sleep(wait)


@bot.message_handler(content_types=['text'])
def send_text(message):
    global onwork
    print(message.chat.username, 'написал', message.text.lower())
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
    elif message.text.lower() == 'отчёт' or message.text.lower() == 'отчет':
        f = open('text.txt', 'r', encoding="utf-8")
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



try:
    print('пулинг')
    bot.polling()
except:
    print('пиздец')
