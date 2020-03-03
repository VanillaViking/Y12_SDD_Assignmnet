import pygame
import threading

from button import *
from animate import animate

class choose_screen():
    def __init__(self, DISPLAY, bg):
        self.background = bg
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)

        self.heading = self.font.render("Choose a pawn color", True, (255,255,255)) 


        #exit button
        self.exit_btn = button([230,230,230, 100],[180,180,180, 190], DISPLAY.get_width() - 60, 10, 50, 50, "X")


        #red_btn        
        self.red_btn = button((255,0,0),(180,0,0), (DISPLAY.get_width()/5) - 50, (DISPLAY.get_height()/2) -50, 100, 100, "", (0,0,0), False)

        #green_btn
        self.green_btn = button((0,255,0),(0,180,0), (DISPLAY.get_width() * 2/5) - 50, (DISPLAY.get_height()/2) -50, 100, 100, "", (0,0,0), False)

        #blue_btn
        self.blue_btn = button((0,0,255),(0,0,180), (DISPLAY.get_width() * 3/5) - 50, (DISPLAY.get_height()/2) -50, 100, 100, "", (0,0,0), False)

        #purple_btn
        self.purple_btn = button((255,0,255),(180,0,180), (DISPLAY.get_width() * 4/5) - 50, (DISPLAY.get_height()/2) -50, 100, 100, "", (0,0,0), False)

    def update_btns(self, btn_event): #runs on separate thread
        while True:
            self.background.draw()

            #heading
            self.display.blit(self.heading, ((self.display.get_width()/2) - (self.heading.get_width() / 2),(self.display.get_height()/4 - (self.heading.get_height()/2)))) 

            #drawing the buttons
            self.exit_btn.draw(self.display)
            self.red_btn.draw(self.display)
            self.purple_btn.draw(self.display)
            self.green_btn.draw(self.display)
            self.blue_btn.draw(self.display)

            for event in pygame.event.get():
                #updating the buttons
                self.exit_btn.update(event)
                self.red_btn.update(event)
                self.blue_btn.update(event)
                self.green_btn.update(event)
                self.purple_btn.update(event)


            pygame.display.update()

            if self.exit_btn.pressed or self.red_btn.pressed or self.blue_btn.pressed or self.green_btn.pressed or self.purple_btn.pressed:
                btn_event.set()
                break

    def draw(self):
        
        #mutlithreading
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        wait_for_press.wait()

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()
            #return the color when pressed
        elif self.red_btn.pressed:
            return (255,0,0)
        elif self.blue_btn.pressed:
            return (0,0,255)
        elif self.green_btn.pressed:
            return (0,255,0)
        elif self.purple_btn.pressed:
            return (255,0,255)








