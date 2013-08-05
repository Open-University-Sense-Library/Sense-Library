import serial, time, binascii, math
from ctypes import c_uint8

#sensor ids
SLIDERID = 0
INFRAREDID = 1
MICROPHONEID = 2
BUTTONID = 3
INPUTAID = 4
INPUTBID = 5
INPUTCID = 6

#other stuff
OUTPUT_HEADER = b"\x54\xFE"

def openPortToSenseboard(portno):
    global ser
    ser = serial.Serial(
        port=portno,
        baudrate=115200,
        timeout=1
        )
    time.sleep(2)

def sendToSenseboard(command, responsesize):
    ser.write(OUTPUT_HEADER + command)
    return ser.read(responsesize)

def ping():
    byte1 = b"\x00"
    byte2 = b"\x00"
    sendToSenseboard(byte1+byte2, 5)
    
def reset():
    byte1 = b"\x10"
    byte2 = b"\x00"
    sendToSenseboard(byte1+byte2, 3)

def turnOffLED(ledid):
    byte1 = b"\xC0"
    byte2 = bytes(c_uint8(2**(ledid-1)))
    sendToSenseboard(byte1 + byte2,3)

def turnOnLED(ledid):
    byte1 = b"\xC1"
    byte2 = bytes(c_uint8(2**(ledid-1)))
    sendToSenseboard(byte1 + byte2,3)

def turnOnMultiLEDs(ledids=[]):
    byte1 = b"\xC1"
    ledint = 0
    for i in range(0,len(ledids),1):
        ledint += 2**(ledids[i]-1)

    byte2 = bytes(c_uint8(ledint))
    sendToSenseboard(byte1 + byte2,3)

def turnOffMultiLEDs(ledids=[]):
    byte1 = b"\xC0"
    ledint = 0
    for i in range(0,len(ledids),1):
        ledint += 2**(ledids[i]-1)

    byte2 = bytes(c_uint8(ledint))
    sendToSenseboard(byte1 + byte2,3)


    byte2 = bytes(c_uint8(ledint))
    sendToSenseboard(byte1 + byte2,3)

def turnOffDCMotor(motorid):
    byte1 = b"\x80"
    byte2 = bytes(c_uint8(motorid))
    sendToSenseboard(byte1 + byte2, 3)

def controlDCMotor(motorid,speed,direction):
    byte1 = bytes(c_uint8(128 + direction))
    byte2 = bytes(c_uint8(32*speed + motorid))
    sendToSenseboard(byte1 + byte2, 3)
    
def setServoPosition(servoid,angle):
    byte1 = bytes(c_uint8(208 + servoid))
    byte2 = bytes(c_uint8(angle))
    sendToSenseboard(byte1 + byte2, 3)

def moveStepper(stepperid, pulses):
    byte1 = bytes(c_uint8(240 + stepperid))
    byte2 = bytes(c_uint8(pulses))
    sendToSenseboard(byte1 + byte2, 3)
    
def readSensor(sensorid):
    byte1 = bytes(c_uint8(32 + sensorid))
    byte2 = bytes(c_uint8(0))
    sinput = sendToSenseboard(byte1 + byte2, 4)
    sinputstr = str(binascii.hexlify(sinput), "ascii")
    sinputint = int(sinputstr[5:], 16)
    return sinputint

def readBursts():
    burstresponse = str(binascii.hexlify(ser.read(size=3*BURSTMODE_SENSOR_AMOUNT)), "ascii")
    return burstresponse

def scaleLEDs(maxv, value, ledno):
    AMOUNT = round((value/maxv) * ledno)
    intarray = []
    for i in range(0, AMOUNT, 1):
            intarray[i-1] = i
            
    turnOnMultiLEDs(intarray)
    

def setBurstMode(sensorids=[]):
    sensorint1 = 0
    sensorint2 = 0
    print(str(len(sensorids)))
    for i in range(0,len(sensorids),1):
        if(sensorids[i] <=7):
            sensorint1 += 2**sensorids[i]
        if(sensorids[i] >7):
            sensorint2 += 2**(sensorids[i]-8)
    global BURSTMODE_SENSOR_AMOUNT
    BURSTMODE_SENSOR_AMOUNT = len(sensorids)
    print(str(BURSTMODE_SENSOR_AMOUNT))
    print(str(sensorint2))
    
    byte1 = b"\xA0"
    byte2 = bytes(c_uint8(sensorint1))
    print(str(binascii.hexlify(byte1+byte2), "ascii"))
    sendToSenseboard(byte1 + byte2, 3)
    
    byte1 = b"\xA1"
    byte2 = bytes(c_uint8(sensorint2))
    print(str(binascii.hexlify(byte1+byte2), "ascii"))
    sendToSenseboard(byte1 + byte2, 3)    

