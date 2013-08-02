import sense
import time

sense.openSerialPort(4)

sense.burstModeSet8to15(1,1,1,0,0,0,0,0)
x=0
while x <10000000:
    print(str(sense.binascii.hexlify(sense.ser.read(size=6)), 'ascii'))
    #time.sleep(0.1)
    x +=1


sense.burstModeOffAll()
