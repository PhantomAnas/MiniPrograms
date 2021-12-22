import psutil 
from pygame import mixer
mixer.init()

mixer.music.set_volume(1) 
from time import sleep
x1 = 'c1.ogg'
x2 = 'c2.ogg'

def batterynotif():
    battery = psutil.sensors_battery().percent

    if battery <= 25:
        mixer.music.load(x1)
        mixer.music.play()

    if battery >= 90:
        mixer.music.load(x2)
        mixer.music.play()

while True:
    batterynotif()
    sleep(4)








