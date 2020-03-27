import configparser
import subprocess
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг

addr = config['settings']['ip_addres']
port = config['settings']['port']
req = config['settings']['xml_request']
resp = config['settings']['xml_response']
log = config['settings']['log_rkeeper']
pasw = config['settings']['pass_rkeeper']
tem = f'xmltest.exe {addr}:{port} {req} {resp} / {log}:{pasw}'
a = subprocess.run (tem, check=True, shell=True, cwd='a',stdout=subprocess.PIPE).stdout.decode(encoding='UTF-8')
if 'Succes' in a:
    print('Отчёт взят')
else:
    print('Не удалось взять отчёт')