import pygame
pygame.init()
pygame.mixer.load('audiopy.mp3')
pygame.mixer.music.play()
pygame.event.wait()