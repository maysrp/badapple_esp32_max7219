import max7219
from machine import Pin, SPI
import json
import time
import os
import urequests
import network
import sdcard

t=time.time()
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# if not wlan.isconnected():
#     wlan.connect('your wifi','passwd')

sdi = SPI(2, baudrate=80000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
sd = sdcard.SDCard(sdi, Pin(22))
sdfile=os.VfsFat(sd)

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(21), mosi=Pin(2))
ss = Pin(5, Pin.OUT)
display = max7219.Matrix8x8(spi,ss,16)

class play():
    def pxy(self,x,y,z,c):
        display.hline(x,y,z,c)
    def image(self,img_list):
        display.fill(img_list[0])
        if img_list[0]==1:
            c=0
        else:
            c=1
        img_list.pop(0)
        for i in img_list:
            self.pxy(i[0],i[1],i[2],c)
        display.show()

display.fill(0)
display.text('Bad Apple    3',0,0,1)
display.show()
time.sleep(1)
display.fill(0)
display.text('Bad Apple    2',0,0,1)
display.show()
time.sleep(1)
display.fill(0)
display.text('Bad Apple    1',0,0,1)
display.show()
time.sleep(1)


Play=play()
z=time.time()
nu=0
old=0
while 1:
    shp=time.time()-z
    if shp>219:
        break
    if old==shp:
        if nu<9:
            nu=nu+1
        else:
            nu=9
            print(old)
    else:
        old=shp
        nu=0
    json_file=sdfile.open(str(shp*10+nu)+'.json','r')
    img_list=json.loads(json_file.read())
    Play.image(img_list)
    if old<28:
        time.sleep(0.09)
    del json_file
    del img_list

zx=time.time()-t
print('Time:',zx)