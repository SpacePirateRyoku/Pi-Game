import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("Running_Free.mp3")
pygame.mixer.music.play()
##while pygame.mixer.music.get_busy() == True:
print("HI")
time.sleep(5)
pygame.mixer.music.stop()
