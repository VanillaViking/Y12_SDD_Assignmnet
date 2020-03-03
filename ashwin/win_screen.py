import pygame
import threading
from button import *
from animate import animate
import time

class win_screen():
    def __init__(self, DISPLAY, bg, winner):
        self.bg = bg
        self.display = DISPLAY
        self.winner = winner
        self.font = pygame.font.SysFont('Arial', 50)


        

        #exit button
        self.exit_btn = button([230,230,230,100],[180,180,180,190], DISPLAY.get_width() - 60, 10, 50, 50, "X")

        #surface to create bg fade illusion
        self.fade_surf = pygame.Surface((self.display.get_width(),self.display.get_height()))
        self.fade_surf.fill(winner.color)

        #heading
        self.heading = self.font.render((self.winner.name + " won!"), True, winner.color)
        
        #back button
        self.bacc_btn = button([230,230,230,100], [180,180,180,190], (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) - 105, 200,100, "Back to Menu")

        #retry button
        self.retry_btn = button([230,230,230,100], [180,180,180,190], (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) +5, 200,100, "Retry")


    def update_btns(self, btn_event):
        while not self.retry_btn.pressed and not self.exit_btn.pressed and not self.bacc_btn.pressed:
            self.bg.draw()

            #heading
            self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))

            self.exit_btn.draw(self.display)
            self.bacc_btn.draw(self.display)
            #self.retry_btn.draw(self.display)

            for event in pygame.event.get():
                self.exit_btn.update(event)
                #self.retry_btn.update(event)
                self.bacc_btn.update(event)
            pygame.display.update()
        btn_event.set()

    def draw(self):

        animate([255], [0], self.anim_heading, [], 120)
        #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        wait_for_press.wait() #waiting for a button to be clicked

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()
        elif self.retry_btn.pressed:
            return 'r'
        else: #else multiplayer
            return 'b'

    def anim_heading(self, start):
        self.fade_surf.set_alpha(int(start[0]))

        self.bg.draw()

        self.exit_btn.draw(self.display)
        self.retry_btn.draw(self.display)
        self.bacc_btn.draw(self.display)

        self.display.blit(self.fade_surf, (0,0))

        self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))
        pygame.display.update()
            

