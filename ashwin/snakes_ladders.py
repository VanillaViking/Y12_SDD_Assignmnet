import pygame
import starting_screen
import choose_color
import player
import board_screen
import bg

def run(DISPLAY):
    #parallax background
    background = bg.parallax_bg(DISPLAY, "ashwin/snek_bg.jpg")

    start_screen = starting_screen.starting_screen(DISPLAY, background)
    choice = start_screen.draw()
    

    if choice == 'sp':
        color_choose = choose_color.choose_screen(DISPLAY, background)
        col = color_choose.draw()
        plyrs = []
        ai_col = (0,255,255)
        plyrs.append(player.player(DISPLAY, col)) #player
        plyrs.append(player.player(DISPLAY, ai_col, True)) #ai

        lol = board_screen.board_screen(DISPLAY, plyrs)
        lol.draw()



