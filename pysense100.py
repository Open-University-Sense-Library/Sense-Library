import serial, time, binascii, os, glob
from ctypes import c_uint8

#sensor ids
SLIDERID = 0
INFRAREDID = 1
MICROPHONEID = 2
BUTTONID = 3
INPUTAID = 4
INPUTBID = 5
INPUTCID = 6

#motor directions
CLOCKWISE = 0
ANTICLOCKWISE = 1

#header
COMMAND_HEADER = b'\x54\xFE'

#object for contolling 1 senseboard
class PySense(object):
    
    ser = serial.Serial()
    burst_length = 0

    def scanWindows(self):
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append( [i, s.portstr] )
                s.close()
            except serial.SerialException:
                pass

        return available
        
    def resetSenseBoard(self):
        global COMMAND_HEADER
        byte_1 = b'\x10'
        byte_2 = b'\x00'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply,'ascii')

    def pingSenseBoard(self):
        global COMMAND_HEADER
        byte_1 = b'\x00'
        byte_2 = b'\x00'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = str(binascii.hexlify(self.ser.read(size=5)),'ascii')
        return reply
    
    def ledOn(self, led_id):
        global COMMAND_HEADER
        byte_1 = b'\xC1'
        byte_2 = bytes(c_uint8(2**(led_id-1)))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        led_id = 0
        return str(reply,'ascii')

    def ledOff(self, led_id):
        global COMMAND_HEADER
        byte_1 = b'\xC0'
        byte_2 = bytes(c_uint8(2**(led_id-1)))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        led_id = 0
        return str(reply,'ascii')
    
    def ledMultiOn(self, led_id_array):
        global COMMAND_HEADER
        led_id_total = 0
        byte_1 = b'\xC1'
        for i in led_id_array:
            led_id_total+=(2**(i-1))
        byte_2 = bytes(c_uint8(led_id_total))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply,'ascii')

    def ledMultiOff(self, led_id_array):
        global COMMAND_HEADER
        led_id_total = 0
        byte_1 = b'\xC0'
        for i in led_id_array:
            led_id_total+=(2**(i-1))
        byte_2 = bytes(c_uint8(led_id_total))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply,'ascii')
    
    def scaleLEDs(self, minvalue, maxvalue, value, ledno):
        AMOUNT = round(((value-minvalue)/(maxvalue-minvalue)) * ledno)
        intarrayon = []
        intarrayoff = []

        for i in range(0, ledno, 1):
            if(i < AMOUNT):
                intarrayon.append(i+1)
            else:
                intarrayoff.append(i+1)

        self.ledMultiOn(intarrayon)
        self.ledMultiOff(intarrayoff)

    def stepperMove(self, motor_id, steps):
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8(240 + motor_id))
        byte_2 = bytes(c_uint8(steps))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply,'ascii')
        

    def servoSetPosition(self, servo_id, angle):
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8(208+ servo_id))
        byte_2 = bytes(c_uint8(angle))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply,'ascii')

    def dcMove(self, motor_id, direction, speed):
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8( 128 + direction ))
        byte_2 = bytes(c_uint8(speed*32 + motor_id))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply,'ascii')
        

    def dcOff(self, motor_id):
        global COMMAND_HEADER
        byte_1 = '\x80'
        byte_2 = bytes(c_uint8(motor_id))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply,'ascii')

    def readSensor(self, sensor_id):
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8(32 + sensor_id))
        byte_2 = b'\x00'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply=binascii.hexlify(self.ser.read(size=4))
        string_reply = str(reply, 'ascii')
        return int(string_reply[5:], 16)

    def burstModeSet(self, sensor_id_array):
        global COMMAND_HEADER
        sensor_id_total_0_to_7 = 0
        sensor_id_total_8_to_15 = 0
        for i in sensor_id_array:
            if i <= 7:
                sensor_id_total_0_to_7 += 2**i

            if i >7:
                sensor_id_total_8_to_15 += 2**i


        byte_1 = b'\xA0'
        byte_2 = bytes(c_uint8(sensor_id_total_0_to_7))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply_1 = binascii.hexlify(self.ser.read(size=3))
        byte_1 = b'\xA1'
        byte_2 = bytes(c_uint8(sensor_id_total_8_to_15))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply_2 = binascii.hexlify(self.ser.read(size=3))
        self.burst_length = len(sensor_id_array)
        if reply_1 == reply_2:
            return str(reply_1,'ascii')
        
    

    def burstModeOffAll(self):
        global COMMAND_HEADER
        byte_1 = b'\xA0'
        byte_2 = b'\x00'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply_1 = binascii.hexlify(self.ser.read(size=3))
        byte_1 = b'\xA1'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply_2 = binascii.hexlify(self.ser.read(size=3))
        if reply_1 == reply_2:
            return str(reply_1,'ascii')
            
        

    def readBursts(self):
        burst_response = str(binascii.hexlify(self.ser.read(size=3*self.burst_length)), 'ascii')
        return burst_response

    def __init__(self):
        if os.name == 'nt':
            for com in self.scanWindows():
                self.ser = serial.Serial(int(com[0]), 115200, timeout=1)
                time.sleep(2)
                if self.pingSenseBoard() == '55ffaa0460':
                    print ("Opening Serial port...")
                    time.sleep(2)
                    print ("Connected to sense at port: " + self.ser.name)
                    break
                else:
                    self.ser.close()

