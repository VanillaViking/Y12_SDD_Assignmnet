import pygame
import threading
from button import *
from animate import animate
import time
import bg

class details_screen():
    def __init__(self, DISPLAY, bg):
        self.bg = bg
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)
        self.num_players = 0

        left_btn = button([255,255,255,100], [255,255, 255,190], (1*DISPLAY.get_width()/2) - 125, (1 * DISPLAY.get_height()/2) - 25, 50, 50, "-")

        right_btn = button([255,255,255,100], [255,255, 255,190], (1*DISPLAY.get_width()/2) + 75, (1 * DISPLAY.get_height()/2) - 25, 50, 50, "+")

        
        self.disp_num = self.font.render(str(self.num_players), True, (255,255,255))

        #exit button
        self.exit_btn = button([230,230,230,100],[180,180,180,190], DISPLAY.get_width() - 60, 10, 50, 50, "X")

        #heading
        self.heading = self.font.render("Number of Players", True, (255,255,255))
        

        self.mp_btn = button([230,230,230,100], [180,180,180,190], (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) +5, 200,100, "Continue")


    def update_btns(self, btn_event):
        while not self.sp_btn.pressed and not self.exit_btn.pressed and not self.mp_btn.pressed:
            self.bg.draw()

            #heading
            self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))
            self.display.blit(self.disp_num, ((self.display.get_width()/2) - (self.disp_num.get_width()/2), (self.display.get_height()/2) - (self.disp_num.get_height()/2)))

            self.exit_btn.draw(self.display)
            self.mp_btn.draw(self.display)
            for event in pygame.event.get():
                self.exit_btn.update(event)
                self.mp_btn.update(event)
            #pygame.display.update([self.exit_btn.rect, self.sp_btn.rect, self.mp_btn.rect])
            pygame.display.update()
        btn_event.set()

    def draw(self):

        #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        wait_for_press.wait() #waiting for a button to be clicked

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()

