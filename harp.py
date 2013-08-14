from pysense100 import *
import time, winsound, _thread


sense1 = PySense()
sense2 = PySense()
sense3 = PySense()
sense4 = PySense()
sense5 = PySense()
sense6 = PySense()
sense7 = PySense()
sense8 = PySense()

sense1.ledOn(7)
sense2.ledOn(7)
sense3.ledOn(7)
sense4.ledOn(7)
sense5.ledOn(7)
sense6.ledOn(7)
sense7.ledOn(7)
sense8.ledOn(7)

def playSound(freq):
    winsound.Beep(freq,1000)

def detectBeamBreak1(note_freq):
    while sense1.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)

def detectBeamBreak2(note_freq):
    while sense2.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)
        
def detectBeamBreak3(note_freq):
    while sense3.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)

def detectBeamBreak4(note_freq):
    while sense4.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)

def detectBeamBreak5(note_freq):
    while sense5.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)

def detectBeamBreak6(note_freq):
    while sense6.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)

def detectBeamBreak7(note_freq):
    while sense7.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)

def detectBeamBreak8(note_freq):
    while sense8.readSensor(INFRAREDID) == 1023:
        playSound(note_freq)
        
_thread.start_new_thread(detectBeamBreak1, (262,))
_thread.start_new_thread(detectBeamBreak2, (294,))
_thread.start_new_thread(detectBeamBreak3, (330,))
_thread.start_new_thread(detectBeamBreak4, (349,))
_thread.start_new_thread(detectBeamBreak5, (392,))
_thread.start_new_thread(detectBeamBreak6, (440,))
_thread.start_new_thread(detectBeamBreak7, (494,))
_thread.start_new_thread(detectBeamBreak8, (523,))

while 1:
    pass
