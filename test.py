import time
import telebot
from multiprocessing import Process

bot = telebot.TeleBot('1048945938:AAHX_0SBJJhwaXkzj-n7OxlFlsxaK6vvFHU')


# так мы обрабатываем команды
@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Commands: /subscribe /unsubscribe /check /help')


# это функция отправки сообщений по таймеру
def check_send_messages():
    while True:
        print('отписка')
        time.sleep(60)


# а теперь запускаем проверку в отдельном потоке
p1 = Process(target=check_send_messages, args=())
p1.start()
p1.join()


while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        # повторяем через 15 секунд в случае недоступности сервера Telegram
        time.sleep(15)