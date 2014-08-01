from pysense import *
import time, pygame.mixer, _thread

sense1 = PySense()
volume = 0
while 1:
        volume = sense1.readSensor(MICROPHONE)
        sense1.scaleLEDs(0,255,volume,6)

