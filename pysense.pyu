import serial, time, binascii
from ctypes import c_uint8



ser = serial.Serial(
    port=3,
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

output_header = b"\x54\xFE"

#sends 4 bytes to senseboard, COMMAND is 2 bytes, header is sent automatically
#RESPONSESIZE is the number of bytes expected as a response, the response is returned
def SendToSenseboard(COMMAND, RESPONSESIZE):
    print("pysense Sent: " + str(binascii.hexlify(COMMAND), "utf-8"))
    ser.write(output_header + COMMAND)
    return ser.read(RESPONSESIZE)

#turns on the led with number LEDID

    
#turns off the led with number LEDID


#returns true if correct response header is recieved

#Resets the senseboard

#Turns off DC Motor, MOTORID 0 and 1 are supported currently

#Allows control of the motor
#DIRECTION is either 1 or 0
#SPEED is 0 to 7
#Only supports MOTORID 1 and 0 on current senseboard version
#def ControlDCMotor(MOTORID, SPEED, DIRECTION):
    #BYTE1 = 128 + DIRECTION #1000 000D
    #BYTE2 =  #PPP0 0MMM
    
def Ping():
    SendToSenseboard(b"\x00\x00", 5)
    
def Reset():
    SendToSenseboard(b"\x10\x00", 3)
    
def TurnOnLED(LEDID):
    LEDVALUE = 2**(LEDID-1)
    SendToSenseboard(b"\xC1" + bytes(c_uint8(LEDVALUE)),3)
    
def TurnOffLED(LEDID):
    LEDVALUE = 2**(LEDID-1)
    SendToSenseboard(b"\xC0" + bytes(c_uint8(LEDVALUE)),3)
    
def TurnOffDCMotor(MOTORID):
    SendToSenseboard(b"\x80" + bytes(c_uint8(LEDVALUE)), 3)

def ControlDCMotor(MOTORID, SPEED, DIRECTION):
    BYTE1 = 128 + DIRECTION #1000 000D
    BYTE2 = 32*SPEED + MOTORID #PPP0 0MMM 
    SendToSenseboard(bytes(c_uint8(BYTE1)) + bytes(c_uint8(BYTE2)), 3)
    
def SetServoPosition(SERVOID, ANGLE):
    BYTE1 = 208 + SERVOID #1101 00SV
    BYTE2 = ANGLE #Angle (AAAA AAAA)
    SendToSenseboard(bytes(c_uint8(BYTE1)) + bytes(c_uint8(BYTE2)), 3)

def MoveStepper(STEPPERID, PULSES):
    BYTE1 = 240 + STEPPERID #1111 00ST
    BYTE2 = PULSES #Pulses (PPPP PPPP)
    SendToSenseboard(bytes(c_uint8(BYTE1)) + bytes(c_uint8(BYTE2)), 3)

def ReadSensor(SENSORID):
    BYTE1 = 32 + SENSORID
    BYTE2 = 0
    INPUT = SendToSenseboard(bytes(c_uint8(BYTE1)) + bytes(c_uint8(BYTE2)), 4)
    
    
#Pings every open port to find the board
#def SearchForSenseboard():
#
#
#

print ("Opening port " + ser.portstr)
time.sleep(2)
MoveStepper(0,60)
time.sleep(.2)
TurnOnLED(1)
time.sleep(.1)
TurnOnLED(2)
time.sleep(.1)
TurnOnLED(3)
time.sleep(.1)
TurnOnLED(4)
time.sleep(.1)
TurnOnLED(5)
time.sleep(.1)
TurnOnLED(6)
time.sleep(.1)
TurnOnLED(7)
time.sleep(.2)
TurnOffLED(1)
time.sleep(2)

#ser.write(output_header + b"\xC1\xFF")
#x=Ping()
#time.sleep(0.1)
#x=binascii.hexlify(x)
#print ("Recieved: " + str(x, "ascii"))
#ser.write(output_header + b"\xC0\xFF")
#time.sleep(0.1)

