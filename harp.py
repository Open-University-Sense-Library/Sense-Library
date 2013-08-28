from pysense100 import *
import time, winsound, _thread


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



root = int(input("please give the frequency of the root:   "))
diminished_second = int (root*((2**(1/12))**0))
minor_second = int (root*((2**(1/12))**1))
major_second = int (root*((2**(1/12))**2))
diminished_third = int (root*((2**(1/12))**2))
augmented_second = int (root*((2**(1/12))**3))
minor_third = int (root*((2**(1/12))**3))
major_third = int (root*((2**(1/12))**4))
diminished_fourth = int (root*((2**(1/12))**4))
augmented_third = int (root*((2**(1/12))**5))
perfect_fourth = int (root*((2**(1/12))**5))
diminished_fifth = int (root*((2**(1/12))**6))
augmented_fourth = int (root*((2**(1/12))**6))
perfect_fifth = int (root*((2**(1/12))**7))
diminished_sixth = int (root*((2**(1/12))**7))
augmented_fifth = int (root*((2**(1/12))**8))
minor_sixth = int (root*((2**(1/12))**9))
diminished_seventh = int (root*((2**(1/12))**9))
major_sixth = int (root*((2**(1/12))**10))
augmented_sixth = int (root*((2**(1/12))**10))
minor_seventh = int (root*((2**(1/12))**10))
major_seventh = int (root*((2**(1/12))**11))
diminished_octave = int (root*((2**(1/12))**11))
augmented_seventh = int (root*((2**(1/12))**12))
octave = int (root*((2**(1/12))**12))

def playTone(freq):
    winsound.Beep(freq,500)

def detectBeamBreak1(note_freq):
    while 1:
        if sense1.readSensor(INFRARED) == 1023:
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
_thread.start_new_thread(detectBeamBreak1, (root,))
_thread.start_new_thread(detectBeamBreak2, (major_second,))
_thread.start_new_thread(detectBeamBreak3, (major_third,))
_thread.start_new_thread(detectBeamBreak4, (perfect_fourth,))
_thread.start_new_thread(detectBeamBreak5, (perfect_fifth,))
_thread.start_new_thread(detectBeamBreak6, (major_sixth,))
_thread.start_new_thread(detectBeamBreak7, (major_seventh,))
#_thread.start_new_thread(detectBeamBreakNone, ())
#_thread.start_new_thread(detectBeamBreak8, (523,))

while 1:
    pass

