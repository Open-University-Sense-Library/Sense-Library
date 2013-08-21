import sense
import time
import winsound
import threading

sense.senseFind()

class SoundThreadClass(threading.Thread):
    def run(self):
        winsound.Beep(440,10000000)


sense.ledOn(7)
sense.burstModeSet([1])
t=SoundThreadClass()
while 1:
    if int (sense.readBursts()[3:],16) == 1023:
        t.stop()
        t.start()
