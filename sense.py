import serial
import time
import binascii
from ctypes import c_uint8

def openSerialPort(port_num):
    print ("Opening Serial port...")
    global ser
    ser = serial.Serial(port_num, 115200,timeout=1 )
    time.sleep(2)
    global command_header
    command_header = b'\x54\xFE'
    print ("Connected to sense at port: " + ser.name)


def ledOn(led):
    led_id=bytes(c_uint8(2**(led-1)))
    ser.write(command_header + b'\xC1' + led_id)
    reply=binascii.hexlify(ser.read(size=3))
    led = 0
    return str(reply,'ascii')
    

def ledOff(led):
    led_id=bytes(c_unit8(2**(led-1)))
    ser.write(command_header + b'\xC0' + led_id)
    reply=binascii.hexlify(ser.read(size=3))
    led = 0
    return str(reply,'ascii')
    

def stepperMove(motor_id, steps):
    byte_1 = bytes(c_uint8(240 + motor_id))
    byte_2 = bytes(c_uint8(steps))
    ser.write(command_header + byte_1 + byte_2)
    reply=binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')
    

def dcMove(direction, speed, motor):
    byte_1 = bytes(c_uint8( 128 + direction ))
    byte_2 = bytes(c_uint8(speed*32 + motor))
    ser.write(command_header + byte_1 + byte_2)
    reply=binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')
    

openSerialPort(4)
dcMove(1, 5, 1)
