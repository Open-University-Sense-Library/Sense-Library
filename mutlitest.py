from pysense import *
import time, pygame.mixer, _thread


sense1, sense2, sense3, sense4, sense5, sense6, sense7 = PySense(), PySense(), PySense(), PySense(), PySense(), PySense(), PySense()
#sense1 = PySense()

sense1.ledOn(1)
sense2.ledOn(2)
sense3.ledOn(3)
sense4.ledOn(4)
sense5.ledOn(5)
sense6.ledOn(6)
sense7.ledOn(7)
