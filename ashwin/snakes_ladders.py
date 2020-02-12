import pygame
import starting_screen
import choose_color

def run(DISPLAY):
    start_screen = starting_screen.starting_screen(DISPLAY)
    start_screen.draw()
    color_choose = choose_color.choose_screen(DISPLAY)
    color_choose.draw()




