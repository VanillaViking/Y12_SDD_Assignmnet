import pygame
import sys

#append the folder to system path:
sys.path.append("ashwin/")

#import game file(s):
import snakes_ladders

pygame.init()

DISPLAY = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#DISPLAY = pygame.display.set_mode((1280,720))


#call start function here
snakes_ladders.run(DISPLAY)
