import datetime
from time import sleep

a = datetime.datetime.now()
sleep(3)
b = datetime.datetime.now()
delta = b - a
print(delta.seconds)