from pysense100 import *
import time

sense1 = PySense()
sense1.ledOn(2)
time.sleep(2)
sense1.ledOff(2)
