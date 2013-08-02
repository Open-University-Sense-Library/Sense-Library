import serial, time, binascii
from ctypes import c_uint8

def openSerialPort(port_num):
    print ("Opening Serial port...")
    global ser
    ser = serial.Serial(port_num, 115200,timeout=1 )
    time.sleep(2)
    global command_header
    command_header = b'\x54\xFE'
    print ("Connected to sense at port: " + ser.name)


def pingSenseBoard():
    byte_1 = b'\x00'
    byte_2 = b'\x00'
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=5))
    return str(reply,'ascii')
    

def resetSenseBoard():
    byte_1 = b'\x10'
    byte_2 = b'\x00'
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=5))
    return str(reply,'ascii')
    

def ledOn(led_id):
    byte_1 = b'\xC1'
    byte_2 = bytes(c_uint8(2**(led_id-1)))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    led_id = 0
    return str(reply,'ascii')
    

def ledMultiOn(led_id_1, led_id_2, led_id_3, led_id_4, led_id_5, led_id_6, led_id_7):
    byte_1 = b'\xC1'
    byte_2 = bytes(c_uint8((led_id_1*(2**0)) + (led_id_2*(2**1)) + (led_id_3*(2**2)) + (led_id_4*(2**3)) + (led_id_5*(2**4)) + (led_id_6*(2**5)) + (led_id_7*(2**6)) ))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    led_id_1, led_id_2, led_id_3, led_id_4, led_id_5, led_id_6, led_id_7 = 0, 0, 0, 0, 0, 0, 0
    return str(reply,'ascii')
    

def ledMultiOff(led_id_1, led_id_2, led_id_3, led_id_4, led_id_5, led_id_6, led_id_7):
    byte_1 = b'\xC0'
    byte_2 = bytes(c_uint8((led_id_1*(2**0)) + (led_id_2*(2**1)) + (led_id_3*(2**2)) + (led_id_4*(2**3)) + (led_id_5*(2**4)) + (led_id_6*(2**5)) + (led_id_7*(2**6)) ))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    led_id_1, led_id_2, led_id_3, led_id_4, led_id_5, led_id_6, led_id_7 = 0, 0, 0, 0, 0, 0, 0
    return str(reply,'ascii')
    

def ledOff(led_id):
    byte_1 = b'\xC0'
    byte_2 = bytes(c_uint8(2**(led_id-1)))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    led = 0
    return str(reply,'ascii')
    

def stepperMove(motor_id, steps):
    byte_1 = bytes(c_uint8(240 + motor_id))
    byte_2 = bytes(c_uint8(steps))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')
    

def servoSetPosition(servo_id, angle):
    byte_1 = bytes(c_uint8(208+ servo))
    byte_2 = bytes(c_uint8(angle))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')


def dcMove(direction, speed, motor_id):
    byte_1 = bytes(c_uint8( 128 + direction ))
    byte_2 = bytes(c_uint8(speed*32 + motor_id))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')
    

def dcOff(motor_id):
    byte_1 = '\x80'
    byte_2 = bytes(c_uint8(motor_id))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')
    

def readSensor(sensor_id):
    '''
    Sensor 0 = Slider 000 - 3ff
    Sensor 1 = IR detector 3ff (not detected), 000 detected 
    Sensor 2 = MIC quiet 000 - 3ff loud
    Sensor 3 = Button 3ff (not pressed) 000 (pressed)
    Sensor 4 = A
    Sensor 5 = B
    Sensor 6 = C
    Sensor 7 - 15 =Nothing
    element         01 23 45 67
    Response code = HH HH IR RR
    H = header
    I = sensor id number
    R = response value
    '''
    byte_1 = bytes(c_uint8(32 + sensor_id))
    byte_2 = b'\x00'
    ser.write(command_header + byte_1 + byte_2)
    reply=binascii.hexlify(ser.read(size=4))
    string_reply = str(reply, 'ascii')
    if sensor_id == 3:
        if int(string_reply[5:], 16) == 1023:
            return False
        else:
            return True
    else:
        return int(string_reply[5:], 16)
        
    

def burstModeSet0to7(sensor_id_0, sensor_id_1, sensor_id_2, sensor_id_3, sensor_id_4, sensor_id_5, sensor_id_6, sensor_id_7):
    byte_1 = b'\xA0'
    byte_2 = bytes(c_uint8((sensor_id_0*(2**0)) + (sensor_id_1*(2**1)) + (sensor_id_2*(2**2)) + (sensor_id_3*(2**3)) + (sensor_id_4*(2**4)) + (sensor_id_5*(2**5)) + (sensor_id_6*(2**6)) + (sensor_id_7*(2**7)) ))
    #print (   binascii.hexlify(  command_header + byte_1 + byte_2  )  )
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    sensor_id_0, sensor_id_1, sensor_id_2, sensor_id_3, sensor_id_4, sensor_id_5, sensor_id_6, sensor_id_7 = 0, 0, 0, 0, 0, 0, 0, 0
    return str(reply,'ascii')
    

def burstModeSet8to15(sensor_id_8, sensor_id_9, sensor_id_10, sensor_id_11, sensor_id_12, sensor_id_13, sensor_id_14, sensor_id_15):
    byte_1 = b'\xA1'
    byte_2 = bytes(c_uint8((sensor_id_8*(2**0)) + (sensor_id_9*(2**1)) + (sensor_id_10*(2**2)) + (sensor_id_11*(2**3)) + (sensor_id_12*(2**4)) + (sensor_id_13*(2**5)) + (sensor_id_14*(2**6)) + (sensor_id_15*(2**7)) ))
    #print (   binascii.hexlify(  command_header + byte_1 + byte_2  )  )
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    sensor_id_8, sensor_id_9, sensor_id_10, sensor_id_11, sensor_id_12, sensor_id_13, sensor_id_14, sensor_id_15 = 0, 0, 0, 0, 0, 0, 0, 0
    return str(reply,'ascii')


def burstModeOffAll():
    byte_1 = b'\xA0'
    byte_2 = b'\x00'
    ser.write(command_header + byte_1 + byte_2)
    reply_1 = binascii.hexlify(ser.read(size=3))
    byte_1 = b'\xA1'
    ser.write(command_header + byte_1 + byte_2)
    reply_2 = binascii.hexlify(ser.read(size=3))
    if reply_1 == reply_2:
        return str(reply_1,'ascii')
        
    

    
