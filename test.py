import sense
import time

sense.openSerialPort(4)

sense.burstModeSet([0,3])
x=0
while x <10000000:
    print(sense.readBursts())
    if sense.readBursts()[9:] == '000' and  int(sense.readBursts()[3:6],16) <= 512:
        sense.stepperMove(0,1)
        time.sleep(0.05)

    elif sense.readBursts()[9:] == '000' and  int(sense.readBursts()[3:6],16) > 512:
        sense.stepperMove(0,-1)
        time.sleep(0.05)
        
    x +=1


sense.burstModeOffAll()
