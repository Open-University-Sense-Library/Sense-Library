import serial
import os
import glob
import sense
'''
def scan():
    """scan for available ports. return a list of device names."""
    return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')


print ("Found ports:")
for name in scan():
    print (str(name))
'''
for i in range(0,32):
    try:
        sense.openSerialPort('/dev/ttyS'+str(i))
        time.sleep(2)
        print('worked!!!')
        serial.close()

    except serial.SerialException:
        print ('nope')
        pass
