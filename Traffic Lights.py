import sense
import pyserial
import binascii
import time

sense.openSerialPort(4)
while 1:
    sense.ledOn(1)
    sense.ledOn(2)
    time.sleep(10)
    
    sense.ledOff(1)
    sense.ledOff(2)
    sense.ledOn(3)
    sense.ledOn(4)
    time.sleep(3)
    
    sense.ledOff(3)
    sense.ledOff(4)
    sense.ledOn(5)
    sense.ledOn(6)
    time.sleep(6)
    
    sense.ledOn(3)
    sense.ledOn(4)
    time.sleep(2)
    
    sense.ledOff(6)
    sense.ledOff(5)
    sense.ledOff(4)
    sense.ledOff(3)

