#!/usr/bin/env python3

from pysense import *
import time, pygame.mixer, _thread


sense1, sense2, sense3, sense4, sense5, sense6, sense7 = PySense(), PySense(), PySense(), PySense(), PySense(), PySense(), PySense()
#sense1 = PySense()

sense1.ledOn(7)
sense2.ledOn(7)
sense3.ledOn(7)
sense4.ledOn(7)
sense5.ledOn(7)
sense6.ledOn(7)
sense7.ledOn(7)
#sense8.ledMultiOn([1,2,3,4,5,6,7])


pygame.mixer.init()

E2 = pygame.mixer.Sound('E2.wav')
E2.set_volume(0.7)
F2 = pygame.mixer.Sound('F2.wav')
Fs2 = pygame.mixer.Sound('F#2.wav')
G2 = pygame.mixer.Sound('G2.wav')
Gs2 = pygame.mixer.Sound('G#2.wav')
A2 = pygame.mixer.Sound('A2.wav')
As2 = pygame.mixer.Sound('A#2.wav')
B2 = pygame.mixer.Sound('B2.wav')
C3 = pygame.mixer.Sound('C3.wav')
Cs3 = pygame.mixer.Sound('C#3.wav')
D3 = pygame.mixer.Sound('D3.wav')
Ds3 = pygame.mixer.Sound('D#3.wav')
E3 = pygame.mixer.Sound('E3.wav')
F3 = pygame.mixer.Sound('F3.wav')
Fs3 = pygame.mixer.Sound('F#3.wav')

def isButtonPressed():
    pass

def detectBeamBreak1(note):
    while 1:
        if sense1.readSensor(INFRARED) == 1023:
            note.play()
            sense1.ledMultiOn([1,2,3,4,5,6])
            while sense1.readSensor(INFRARED) == 1023:
                pass
        note.stop()
        sense1.ledMultiOff([1,2,3,4,5,6])

def detectBeamBreak2(note):
    while 1:
        if sense2.readSensor(INFRARED) == 1023:
            note.play()
            sense2.ledMultiOn([1,2,3,4,5,6])
            while sense2.readSensor(INFRARED) == 1023:
                pass
        note.stop()
        sense2.ledMultiOff([1,2,3,4,5,6])
        
def detectBeamBreak3(note):
    while 1:
        if sense3.readSensor(INFRARED) == 1023:
            note.play()
            sense3.ledMultiOn([1,2,3,4,5,6])
            while sense3.readSensor(INFRARED) == 1023:
                pass
        note.stop()
        sense3.ledMultiOff([1,2,3,4,5,6])

def detectBeamBreak4(note):
    while 1:
        if sense4.readSensor(INFRARED) == 1023:
            note.play()
            sense4.ledMultiOn([1,2,3,4,5,6])
            while sense4.readSensor(INFRARED) == 1023:
                pass
        note.stop()
        sense4.ledMultiOff([1,2,3,4,5,6])

def detectBeamBreak5(note):
    while 1:
        if sense5.readSensor(INFRARED) == 1023:
            note.play()
            sense5.ledMultiOn([1,2,3,4,5,6])
            while sense5.readSensor(INFRARED) == 1023:
                pass
        note.stop()
        sense5.ledMultiOff([1,2,3,4,5,6])

def detectBeamBreak6(note):
    while 1:
        if sense6.readSensor(INFRARED) == 1023:
            note.play()
            sense6.ledMultiOn([1,2,3,4,5,6])
            while sense6.readSensor(INFRARED) == 1023:
                pass
        note.stop()
        sense6.ledMultiOff([1,2,3,4,5,6])

def detectBeamBreak7(note):
    while 1:
        if sense7.readSensor(INFRARED) == 1023:
            note.play()
            sense7.ledMultiOn([1,2,3,4,5,6])
            while sense7.readSensor(INFRARED) == 1023:
                pass
        note.stop()
        sense7.ledMultiOff([1,2,3,4,5,6])


'''
def detectBeamBreak8(note_freq):
    while 1:
        while sense8.readSensor(INFRARED) == 1023:
            playTone(note_freq)

'''        
_thread.start_new_thread(detectBeamBreak1, (E2,))
_thread.start_new_thread(detectBeamBreak2, (Fs2,))
_thread.start_new_thread(detectBeamBreak3, (Gs2,))
_thread.start_new_thread(detectBeamBreak4, (A2,))
_thread.start_new_thread(detectBeamBreak5, (B2,))
_thread.start_new_thread(detectBeamBreak6, (Cs3,))
_thread.start_new_thread(detectBeamBreak7, (Ds3,))
#_thread.start_new_thread(detectBeamBreak8, (E3,))
while 1:
    pass

