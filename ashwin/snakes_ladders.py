import pygame
import starting_screen
import choose_color
import player
import board_screen
import bg
import win_screen

def run(DISPLAY):
    #parallax background
    background = bg.parallax_bg(DISPLAY, "ashwin/snek_bg.jpg")

    start_screen = starting_screen.starting_screen(DISPLAY, background)
    choice = start_screen.draw()
    

    if choice == 'sp': #singleplayer agains AI
        color_choose = choose_color.choose_screen(DISPLAY, background)
        col = color_choose.draw()
        plyrs = []
        ai_col = (0,255,255)
        plyrs.append(player.player(DISPLAY, "You", col)) #player
        plyrs.append(player.player(DISPLAY, "AI", ai_col, True)) #ai

        bored = board_screen.board_screen(DISPLAY, plyrs)
        bored.draw()

        w_screen = win_screen.win_screen(DISPLAY, background, bored.winner)
        w_screen.draw()
        


        



