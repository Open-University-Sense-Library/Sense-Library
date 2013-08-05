import sense
import time

sense.openSerialPort(4)
while 1:
    sense.ledMultiOn([1,2])
    time.sleep(10)

    sense.ledMultiOff([1,2])
    sense.ledMultiOn([3,4])
    time.sleep(3)
    
    sense.ledMultiOff([3,4])
    sense.ledMultiOn([5,6])
    time.sleep(6)
    
    sense.ledMultiOn([3,4])
    time.sleep(2)
    
    sense.ledMultiOff([3,4,5,6])

