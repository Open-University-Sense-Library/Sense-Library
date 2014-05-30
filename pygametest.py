import pygame, time

pygame.mixer.init()
sound = pygame.mixer.Sound('E2.wav')
sound.play()
time.sleep(2)
