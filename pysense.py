import serial, time, binascii, os, glob
from ctypes import c_uint8


#sensor IDs used to select sensor to read

SLIDER = 0
INFRARED = 1
MICROPHONE = 2
BUTTON = 3
INPUT_A = 4
INPUT_B = 5
INPUT_C = 6
INPUT_D = 7

#motor directions
CLOCKWISE = 0
ANTICLOCKWISE = 1

#header which is prefixed to all commands
COMMAND_HEADER = b'\x54\xFE'

#make empty array for linux port list
PORTLIST = []

#class for controlling individual SenseBoards
class PySense(object):
    
    ser = serial.Serial()
    burst_length = 0
	
    def scanWindows(self): #generates array of available ports on windows
        available = []
        for i in range(256):
            try: #try establishing connection to COM ports up to 256
                s = serial.Serial(i)
                available.append( [i, s.portstr] ) #if port is connected to successfully append port number and name to available array
                s.close()
            except serial.SerialException:
                pass

        return available
	
    def scanPosix(self): #generates array of available ports on linux
        global PORTLIST
        if len(PORTLIST) == 0:
            PORTLIST =  glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
			#if PORTLIST hasn't been defined, add all available ports to array
        
        #print (PORTLIST)
        return PORTLIST #returns array of ports now defined in global variable PORTLIST

    def resetSenseBoard(self): #resets SenseBoard - turns all LEDs and motors off etc.
        global COMMAND_HEADER
        byte_1 = b'\x10'
        byte_2 = b'\x00' #define bytes 1 and 2 to be sent to perform command
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2) #send all bytes to board
        reply = binascii.hexlify(self.ser.read(size=3)) #read reply from board
        return str(reply, 'ascii') #return reply as ascii string
        

    def pingSenseBoard(self): #pings SenseBoard
        global COMMAND_HEADER
        byte_1 = b'\x00'
        byte_2 = b'\x00' #define bytes 1 and 2 to be sent to perform command
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2) #send all bytes to board
        reply = binascii.hexlify(self.ser.read(size=5)) #read reply from board
        return str(reply, 'ascii') #return reply as ascii string
    
    def ledOn(self, led_id): #turns ON an individual LED - takes LED number as an int
        global COMMAND_HEADER
        byte_1 = b'\xC1'
        byte_2 = bytes(c_uint8(2**(led_id-1)))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        led_id = 0 #resets id to 0
        return str(reply, 'ascii') #return reply as ascii string

    def ledOff(self, led_id): #turns OFF an individual LED - takes LED number as an int
        global COMMAND_HEADER
        byte_1 = b'\xC0'
        byte_2 = bytes(c_uint8(2**(led_id-1)))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        led_id = 0 #resets id to 0
        return str(reply, 'ascii') #return reply as ascii string
    
    def ledMultiOn(self, led_id_array): #turns ON multiple LEDs - takes LED numbers as an array of ints
        global COMMAND_HEADER
        led_id_total = 0 #clear led list
        byte_1 = b'\xC1'
        for i in led_id_array:
            led_id_total+=(2**(i-1))
        byte_2 = bytes(c_uint8(led_id_total))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply, 'ascii') #return reply as ascii string
    
    def ledMultiOff(self, led_id_array): #turns OFF multiple LEDs - takes LED numbers as an array of ints
        global COMMAND_HEADER
        led_id_total = 0 #clear led list
        byte_1 = b'\xC0'
        for i in led_id_array:
            led_id_total+=(2**(i-1))
        byte_2 = bytes(c_uint8(led_id_total))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply, 'ascii') #return reply as ascii string
    
    def scaleLEDs(self, minvalue, maxvalue, value, maxled): #turns ON multiple LEDs depending on size of value input compared to minvalue and maxvalue e.g. scaleLEDs(0,100,50,6) will turn on (50/100) of the LEDs up to LED 6
        AMOUNT = round(((value - minvalue)/(maxvalue - minvalue)) * maxled)
        intarrayon = []
        intarrayoff = []

        for i in range(0, maxled, 1):
            if(i < AMOUNT):
                intarrayon.append(i+1)
            else:
                intarrayoff.append(i+1)

        self.ledMultiOn(intarrayon)
        self.ledMultiOff(intarrayoff)
        

    def stepperMove(self, motor_id, steps): #turns on stepper motor for input number of steps
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8(240 + motor_id))
        byte_2 = bytes(c_uint8(steps))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply, 'ascii') #return reply as ascii string
    
    def servoSetPosition(self, servo_id, angle): #sets servo to input position
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8(208+ servo_id))
        byte_2 = bytes(c_uint8(angle))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply, 'ascii') #return reply as ascii string

    def dcMove(self, motor_id, direction, speed): #turns ON motor giving direction and speed
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8( 128 + direction ))
        byte_2 = bytes(c_uint8(speed*32 + motor_id))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply, 'ascii') #return reply as ascii string
    
    def dcOff(self, motor_id): #turns OFF motor
        global COMMAND_HEADER
        byte_1 = '\x80'
        byte_2 = bytes(c_uint8(motor_id))
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply = binascii.hexlify(self.ser.read(size=3))
        return str(reply, 'ascii') #return reply as ascii string
    
    def readSensor(self, sensor_id): #gives reading of sensor between 0 and 255 as an int
        global COMMAND_HEADER
        byte_1 = bytes(c_uint8(32 + sensor_id))
        byte_2 = b'\x00'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply=binascii.hexlify(self.ser.read(size=4))
        string_reply = str(reply, 'ascii')
        return int(string_reply[5:], 16) #return return value of sensor as int
    
    def burstModeSet(self, sensor_id_array): #turns on burst mode for input array of sensors
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
            return str(reply_1, 'ascii')  #return reply as ascii string
    
    def burstModeOffAll(self): #turns OFF burst mode for all sensors
        global COMMAND_HEADER
        byte_1 = b'\xA0'
        byte_2 = b'\x00'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply_1 = binascii.hexlify(self.ser.read(size=3))
        byte_1 = b'\xA1'
        self.ser.write(COMMAND_HEADER + byte_1 + byte_2)
        reply_2 = binascii.hexlify(self.ser.read(size=3))
        if reply_1 == reply_2:
            return str(reply_1, 'ascii')  #return reply as ascii string
    
    def readBursts(self): #returns all responses of sensors with burst mode on WARNING CAN BE INTERUPTED BY SENDING OR RECEIVING DATA WHILE READING
        burst_response = binascii.hexlify(self.ser.read(size=3*self.burst_length))
        return str(burst_repsonse, 'ascii')  #return all data being sent back from burst mode as ascii string


    def __init__(self): #class initialisation
        global PORTLIST
        if os.name == 'nt': #if on windows
            for com in self.scanWindows(): #call scanWindows method 
                self.ser = serial.Serial(int(com[0]), 115200, timeout=1)
                time.sleep(2)
                if self.pingSenseBoard() == '55ffaa0460':
                    print ("Opening Serial port...")
                    time.sleep(2)
                    print ("Connected to sense at port: " + self.ser.name)
                    break
                else:
                    self.ser.close()
					
        elif os.name == 'posix': #if on linux or mac based OS
            for com in self.scanPosix():
                try:
                    self.ser = serial.Serial(com, 115200, timeout=1)
                    print ("trying to connect to " + str(com))
                    time.sleep(2)
                    if self.pingSenseBoard() == '55ffaa0460':
                        print ("Opening Serial port...")
                        print ("Connected to sense at port:" + self.ser.name)
                        PORTLIST.remove(com)
                        break
                    else:
                        print ("This isn't a SenseBoard, closing port")
                        self.ser.close()

                except serial.SerialException:
                    pass
                
