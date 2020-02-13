import pygame
import starting_screen
import choose_color
import player
import board_screen

def run(DISPLAY):

    start_screen = starting_screen.starting_screen(DISPLAY)
    start_screen.draw()

    color_choose = choose_color.choose_screen(DISPLAY)
    col = color_choose.draw()
    plyrs = []
    plyrs.append(player.player(DISPLAY, col))

    lol = board_screen.board_screen(DISPLAY, plyrs)
    lol.draw()



