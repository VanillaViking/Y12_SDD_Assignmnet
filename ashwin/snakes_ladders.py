import pygame
import starting_screen
import choose_color
import player
import board_screen

def run(DISPLAY):

    start_screen = starting_screen.starting_screen(DISPLAY)
    choice = start_screen.draw()
    print(choice)

    if choice == 'sp':
        color_choose = choose_color.choose_screen(DISPLAY)
        col = color_choose.draw()
        plyrs = []
        ai_col = (0,255,255)
        plyrs.append(player.player(DISPLAY, col)) #player
        plyrs.append(player.player(DISPLAY, ai_col, True)) #ai

        lol = board_screen.board_screen(DISPLAY, plyrs)
        lol.draw()



