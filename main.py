import time
import telebot
from telebot import types
import threading
from bs4 import BeautifulSoup
import subprocess
from XMLpars import xmlpars

bot = telebot.TeleBot('1048945938:AAHX_0SBJJhwaXkzj-n7OxlFlsxaK6vvFHU', threaded=True)  # Инициализация бота
menu_markup = 'markup_report'
markup_start = types.ReplyKeyboardMarkup(row_width=2)
markup_start.add('Привет')
markup_start.add('Подписки на расслыки')
markup_start.add('Отчёт')
markup_start.add('Пока')

markup_send_al = types.ReplyKeyboardMarkup(row_width=2)
markup_send_al.add('Подписки-> скидки')
markup_send_al.add('Назад->')


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
        xml_work()
        bot.send_message(message.chat.id, 'Отчёт сформирован')

    elif message.text.lower() == 'подписки на расслыки':  # Вывод меню для подписок

        bot.send_message(message.chat.id, 'выберите тип подписки', reply_markup=markup_send_al)
        menu_markup = 'markup_send_al'

    elif message.text.lower() == 'назад->':  # Вывод меню для получения отчёта
        if menu_markup == 'markup_report':
            bot.send_message(message.chat.id, 'назад ', reply_markup=markup_start)
        elif menu_markup == 'markup_send_al':
            bot.send_message(message.chat.id, 'назад ', reply_markup=markup_start)
        elif menu_markup == 'markup_cancel_send':
            bot.send_message(message.chat.id, 'назад ', reply_markup=markup_send_al)
            menu_markup = 'markup_send_al'

    elif message.text.lower() == 'отчёт':  # Вывод меню для получения отчёта
        markup_report = types.ReplyKeyboardMarkup(row_width=2)
        markup_report.add('Отчёт->операции')
        markup_report.add('Отчёт->скидки')
        markup_report.add('Отчёт->сформировать')
        markup_report.add('Назад->')
        bot.send_message(message.chat.id, 'выберите тип отчёта', reply_markup=markup_report)
        menu_markup = 'markup_report'

    elif message.text.lower() == 'отписаться->скидки':
        file = open('send_disc.txt', 'r', encoding='UTF-8')
        mans = file.readlines()
        del_man = str(message.chat.id)
        file.close()
        if len(mans) > 1:
            for i in range(0, len(mans) - 1):
                print(f'проверяем {mans[i]} с {del_man}')
                if del_man == str(mans[i]).strip():
                    del mans[i]
                    bot.send_message(message.chat.id, 'Вы отписались', reply_markup=markup_send_al)
                    file = open('send_disc.txt', 'w', encoding='UTF-8')
                    for man in mans:
                        file.write(man)
                    break
        elif len(mans) == 1:
            if del_man == str(mans[0]).strip():
                del mans[0]
                bot.send_message(message.chat.id, 'Вы отписались', reply_markup=markup_send_al)
                file = open('send_disc.txt', 'w', encoding='UTF-8')
                for man in mans:
                    file.write(man)

    elif message.text.lower() == 'подписки-> скидки':
        file = open('send_disc.txt', 'r', encoding='UTF-8')
        mans = file.readlines()
        file.close()
        file = open('send_disc.txt', 'a', encoding='UTF-8')
        have = False
        new_man = str(message.chat.id)
        if len(mans) > 1:
            for i in range(0, len(mans) - 1):
                man = str(mans[i].strip())
                print(f'Проверяем {man} на совпадение с {new_man}')
                if man == new_man:
                    have = True
                    break
        if len(mans) == 1:
            man = str(mans[0].strip())
            print(f'Проверяем {man} на совпадение с {new_man}')
            if man == new_man:
                have = True
        if have:
            file.close()
            markup_cancel_send = types.ReplyKeyboardMarkup(row_width=2)
            markup_cancel_send.add('Отписаться->скидки')
            markup_cancel_send.add('Назад->')
            menu_markup = 'markup_cancel_send'
            bot.send_message(message.chat.id, 'вы уже подписаны, отписаться?', reply_markup=markup_cancel_send)
        else:
            bot.send_message(message.chat.id, 'Вы добавлены в список рассылки')
            file.write(new_man + '\n')
            file.close()

    elif message.text.lower() == 'отчёт->скидки' or message.text.lower() == 'отчет->скидки':  # Вывод отчёта по скидкам
        f = open('Скидки.txt', 'r', encoding="utf-8")
        a = f.read()
        if len(a) != 0:
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


def send_new_alarm(message):
    file = open('send_disc.txt', 'r', encoding='UTF-8')
    mans = file.readlines()
    for man in mans:
        manw = str(man).strip()
        bot.send_message(manw, message)


def send_func():
    while True:
        try:
            print('запуск парсера')
            xml_work()
            time.sleep(30)
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


def xml_work():
    file = open('посл_скидка.txt', 'r', encoding='UTF-8')
    last_disc = file.read()
    file.close()
    a = open('a/as1.bat').read()
    try:
        subprocess.run(a, check=True, shell=True, cwd='a')
        print('Отчёт взят')

    except:
        print('Не получилось взять отчёт')
    count = int(0)
    operation = str(open('a/response.xml', 'r', encoding="utf-8").read())
    a = open('Операции.txt', 'w', encoding="utf-8")
    soup = BeautifulSoup(operation, 'lxml')
    operations = soup.find_all('row')
    lists = []
    for operation in operations:
        if count == 0:
            a.write('*****ОПЕРАЦИИ*****' + '\n')
            count = + 1

        if operation.get('datetime') != '':
            # print(operation.get('datetime'), operation.get('operation'), operation.get('operator'))
            c = str(
                operation.get('datetime') + ' ' + operation.get('operation') + ' ' + operation.get('operator') + '\n')
            lists.append(c)

    sort_list = sorted(lists)
    if len(sort_list) != 0:
        for st in sort_list:
            a.write(st)
    lists = []
    count = int(0)
    a.close()
    t = open('Скидки.txt', 'w', encoding="utf-8")
    discounts = soup.find_all('skidk')

    for discount in discounts:
        if count == 0:
            t.write('*****СКИДКИ*****' + '\n')
            count = + 1
        if discount.get('discount') != 0:
            for operation in operations:
                if operation.get('visit') == discount.get('visit'):
                    bolls = True
                    break
            c = str(operation.get('datetime') + ' ' + discount.get('discount') + ' ' + discount.get(
                'author') + ' ' + discount.get('sum') + ' ' + discount.get(
                'chargesource') + '\n')
            if last_disc == '':
                last_disc = operation.get('datetime')
            elif last_disc < operation.get('datetime'):
                send_new_alarm(c)
                last_disc = operation.get('datetime')
                print('последнее время', last_disc)
        lists.append(c)

    sort_list = sorted(lists)
    last_file = open('посл_скидка.txt', 'w', encoding='UTF-8')
    last_file.write(last_disc)
    if len(sort_list) != 0:
        for st in sort_list:
            t.write(st)
    t.close()
    print('отчёт сформирован')


p2 = threading.Thread(target=polling, args=())
p1 = threading.Thread(target=send_func, args=())
p2.start()
p1.start()
p2.join()
p1.join()
