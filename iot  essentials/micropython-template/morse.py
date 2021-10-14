from machine import Pin
from time import sleep

p2 = Pin(2, Pin.OUT)
p2.value(False)

inp = list(input("Enter a morse code:"))

for item in inp:
    if item == '0':
        # blink for 0.2 sec
        p2.value(True)
        sleep(0.2)
        p2.value(False)
        sleep(0.1)
    else:
        # blink for 0.8 sec
        p2.value(True)
        sleep(0.8)
        p2.value(False)
        sleep(0.1)