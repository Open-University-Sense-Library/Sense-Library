from objectPysense import *
import time

senseboard1 = PySense()

senseboard2 = PySense()

senseboard3 = PySense()

senseboard4 = PySense()

testy = 0
while 1:
    testy = int((senseboard1.readSensor(0)/1023) * 800)
    senseboard1.scaleLEDs(0, 200, testy, 7)
    senseboard2.scaleLEDs(200, 400, testy, 7)
    senseboard3.scaleLEDs(400, 600, testy, 7)
    senseboard4.scaleLEDs(600, 800, testy, 7)
