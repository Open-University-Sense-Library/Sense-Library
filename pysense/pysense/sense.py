import serial, time, binascii
from ctypes import c_uint8

def scan():
    available = []
    for i in range(256):
        try:
            s = serial.Serial(i)
            available.append( [i, s.portstr] )
            s.close()
        except serial.SerialException:
            pass

    return available

def senseFind():
    global ser
    global command_header
    command_header = b'\x54\xFE'
    for com in scan():
        ser = serial.Serial(int(com[0]), 115200, timeout=1)
        time.sleep(2)
        if pingSenseBoard() == '55ffaa0460':
            print ("Opening Serial port...")
            time.sleep(2)
            print ("Connected to sense at port: " + ser.name)
            break
        else:
            ser.close()
            



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
    reply = str(binascii.hexlify(ser.read(size=5)),'ascii')
    return reply
    

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
    

def ledMultiOn(led_id_array):
    led_id_total = 0
    byte_1 = b'\xC1'
    for i in led_id_array:
        led_id_total+=(2**(i-1))
    byte_2 = bytes(c_uint8(led_id_total))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')
    

def ledMultiOff(led_id_array):
    led_id_total = 0
    byte_1 = b'\xC0'
    for i in led_id_array:
        led_id_total+=(2**(i-1))
    byte_2 = bytes(c_uint8(led_id_total))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
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
    byte_1 = bytes(c_uint8(208+ servo_id))
    byte_2 = bytes(c_uint8(angle))
    ser.write(command_header + byte_1 + byte_2)
    reply = binascii.hexlify(ser.read(size=3))
    return str(reply,'ascii')

def dcMove(motor_id, direction, speed):
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
        
    

def burstModeSet(sensor_id_array):
    sensor_id_total_0_to_7 = 0
    sensor_id_total_8_to_15 = 0
    for i in sensor_id_array:
        if i <= 7:
            sensor_id_total_0_to_7 += 2**i

        if i >7:
            sensor_id_total_8_to_15 += 2**i


    byte_1 = b'\xA0'
    byte_2 = bytes(c_uint8(sensor_id_total_0_to_7))
    ser.write(command_header + byte_1 + byte_2)
    reply_1 = binascii.hexlify(ser.read(size=3))
    byte_1 = b'\xA1'
    byte_2 = bytes(c_uint8(sensor_id_total_8_to_15))
    ser.write(command_header + byte_1 + byte_2)
    reply_2 = binascii.hexlify(ser.read(size=3))
    global burst_length
    burst_length = len(sensor_id_array)
    if reply_1 == reply_2:
        return str(reply_1,'ascii')
        
    

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
        
    

def readBursts():
    burst_response = str(binascii.hexlify(ser.read(size=3*burst_length)), 'ascii')
    return burst_response
