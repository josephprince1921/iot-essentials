import os
from machine import Pin, SoftSPI
from sdcard import SDCard

Pin(2, Pin.OUT).value(True)

# Pin assignment:
# MISO -> GPIO 13
# MOSI -> GPIO 12
# SCK  -> GPIO 14
# CS   -> GPIO 27
spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))
sd = SDCard(spisd, Pin(27))


print('Root directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
print('SD Card contains:{}'.format(os.listdir()))


# 1. To read file from the root directory:
f = open('t.csv', 'r')
print(f.read())
f.close()

from machine import I2C
os.chdir('/')
import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(19), scl=Pin(18))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello, World!', 0, 0, 1)
display.show()