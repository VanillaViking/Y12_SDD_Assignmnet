import pygame
import sys

#append the folder to system path:
sys.path.append("ashwin/")

#import game file(s):
import snakes_ladders

pygame.init()

DISPLAY = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

DISPLAY.fill((255,255,255))

#call start function here
