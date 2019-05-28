# badapple_esp32_max7219
esp32  Micropython Max7219 

[视频地址](https://www.bilibili.com/video/av53892585)

+ SDcard卡槽  

+ max7219 LED点阵 8x8 16块

+ ESP32

将badapple里面的JSON文件保存到你的SD卡中将SD卡槽与你的ESP32通过SPI通信，MAX7219连接后也与你的ESP32连接，上传sdcard.py和boot.py和max7219到你的ESP32中。即可播放badapple


SDcard|ESP32
|-|-|
vcc|3v3
GDN|GDN
SD_MISO|D19
SD_MOSI|D23
SD_SCK|D18
SD_CS|D22

MAX7219|ESP32
|-|-|
VCC|Vin
GDN|GDN
DIN|D2
CLK|D21
CS|D5


另外备注下面两个文件来自以下的两个项目  

[max7219.py](https://github.com/mcauser/micropython-max7219)

[scard.py](https://github.com/zhangxuhong1024/wifi2can)


