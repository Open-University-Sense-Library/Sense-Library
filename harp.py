from pysense100 import *
import time, pygame.mixer, _thread


sense1, sense2, sense3, sense4, sense5, sense6, sense7 = PySense(), PySense(), PySense(), PySense(), PySense(), PySense(), PySense()

sense1.ledOn(7)
sense2.ledOn(7)
sense3.ledOn(7)
sense4.ledOn(7)
sense5.ledOn(7)
sense6.ledOn(7)
sense7.ledOn(7)
#sense8.ledMultiOn([1,2,3,4,5,6,7])
is_playing = False

def playTone(freq):
    winsound.Beep(freq,1000)

def detectBeamBreak1(note_freq):
    while 1:
        while sense1.readSensor(INFRARED) == 1023:
            playTone(note_freq)
            is_playing = True

def detectBeamBreak2(note_freq):
    while 1:
        while sense2.readSensor(INFRARED) == 1023:
            playTone(note_freq)
            is_playing = True
        
def detectBeamBreak3(note_freq):
    while 1:
        while sense3.readSensor(INFRARED) == 1023:
            playTone(note_freq)
            is_playing = True

def detectBeamBreak4(note_freq):
    while 1:
        while sense4.readSensor(INFRARED) == 1023:
            playTone(note_freq)
            is_playing = True

def detectBeamBreak5(note_freq):
    while 1:
        while sense5.readSensor(INFRARED) == 1023:
            playTone(note_freq)
            is_playing = True

def detectBeamBreak6(note_freq):
    while 1:
        while sense6.readSensor(INFRARED) == 1023:
            playTone(note_freq)
            is_playing = True

def detectBeamBreak7(note_freq):
    while 1:
        while sense7.readSensor(INFRARED) == 1023:
            playTone(note_freq)
            is_playing = True
'''
def detectBeamBreakNone():
    while 1:
       while is_playing == False:
            winsound.PlaySound(None, winsound.SND_NODEFAULT)
'''
'''
def detectBeamBreak8(note_freq):
    while 1:
        while sense8.readSensor(INFRARED) == 1023:
            playTone(note_freq)

'''        
_thread.start_new_thread(detectBeamBreak1, (262,))
_thread.start_new_thread(detectBeamBreak2, (294,))
_thread.start_new_thread(detectBeamBreak3, (330,))
_thread.start_new_thread(detectBeamBreak4, (349,))
_thread.start_new_thread(detectBeamBreak5, (392,))
_thread.start_new_thread(detectBeamBreak6, (440,))
_thread.start_new_thread(detectBeamBreak7, (494,))
#_thread.start_new_thread(detectBeamBreakNone, ())
#_thread.start_new_thread(detectBeamBreak8, (523,))

while 1:
    pass

