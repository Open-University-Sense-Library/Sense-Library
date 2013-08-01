import serial, time, binascii
from ctypes import c_uint8

def openSerialPort(port_num):
    print ("Opening Serial port...")
    global SER
    SER = serial.Serial(port_num, 115200,timeout=1 )
    time.sleep(2)
    global COMMAND_HEADER
    COMMAND_HEADER = b'\x54\xFE'
    print ("Connected to sense at port: " + SER.name)


def pingSenseBoard():
    byte_1 = b'\x00'
    byte_2 = b'\x00'
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=5))
    return str(reply,'ascii')
    

def resetSenseBoard():
    byte_1 = b'\x10'
    byte_2 = b'\x00'
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=5))
    return str(reply,'ascii')
    

def ledOn(led_id):
    byte_1 = b'\xC1'
    byte_2 = bytes(c_uint8(2**(led_id-1)))
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=3))
    led = 0
    return str(reply,'ascii')
    

def ledOff(led_id):
    byte_1 = b'\xC0'
    byte_2 = bytes(c_unit8(2**(led_id-1)))
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=3))
    led = 0
    return str(reply,'ascii')
    

def stepperMove(motor_id, steps):
    byte_1 = bytes(c_uint8(240 + motor_id))
    byte_2 = bytes(c_uint8(steps))
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=3))
    return str(reply,'ascii')
    

def servoSetPosition(servo_id, angle):
    byte_1 = bytes(c_uint8(208+ servo))
    byte_2 = bytes(c_unit8(angle))
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=3))
    return str(reply,'ascii')


def dcMove(direction, speed, motor_id):
    byte_1 = bytes(c_uint8( 128 + direction ))
    byte_2 = bytes(c_uint8(speed*32 + motor_id))
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=3))
    return str(reply,'ascii')
    

def dcOff(motor_id):
    byte_1 = '\x80'
    byte_2 = bytes(c_uint(motor_id))
    SER.write(COMMAND_HEADER + byte_1 + byte_2)
    reply=binascii.hexlify(SER.read(size=3))
    return str(reply,'ascii')
    

