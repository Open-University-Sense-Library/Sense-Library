import sense
import time
import winsound

sense.senseFind()

sense.ledOn(7)
sense.burstModeSet([1])
while 1:
    while sense.readBursts()[3:]
