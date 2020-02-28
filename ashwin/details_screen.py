import pygame
import threading
from button import *
from text_input import *
from animate import animate
import time
import bg

class details_screen():
    def __init__(self, DISPLAY, bg):
        self.bg = bg
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)
        self.sfont = pygame.font.SysFont('Arial', 30)
        self.stop = False
        self.show_err = False

        self.text1 = self.sfont.render("Player Names (separated by comma)", True, (200,200,200)).convert_alpha()
        self.name = text_input(DISPLAY, (DISPLAY.get_width()/2) + 10, (DISPLAY.get_height()/2) -25, 500, 50, '', (255,255,255))

        #input error msg
        self.err = self.sfont.render("only playable with 2 to 4 players", True, (255,0,0,0)).convert_alpha()

        #exit button
        self.exit_btn = button([230,230,230,100],[180,180,180,190], DISPLAY.get_width() - 60, 10, 50, 50, "X")

        #heading
        self.heading = self.font.render("Number of Players", True, (255,255,255)).convert_alpha()  

        #continue button 
        self.cont_btn = button([230,230,230,100], [180,180,180,190], (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) +5, 200,100, "Continue")


    def update_btns(self, btn_event):
        while not self.stop:
            #drawing all elements onto screen

            self.bg.draw()
            self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))

            self.display.blit(self.text1, ((self.display.get_width() / 2) - 10 - (self.text1.get_width()),(self.display.get_height()/2) - self.text1.get_height()/2))

            self.name.draw()

            self.exit_btn.draw(self.display)
            self.cont_btn.draw(self.display)

            if self.show_err:
                self.display.blit(self.err, ((self.display.get_width()/2)-(self.err.get_width()/2),(self.display.get_height() * 3/5)-(self.err.get_height()/2)))

            for event in pygame.event.get():
                self.exit_btn.update(event)
                self.cont_btn.update(event)
                self.name.activate(event)

            pygame.display.update()

            if self.cont_btn.pressed:
                btn_event.set()
            elif self.exit_btn.pressed:
                btn_event.set()
                break

    def draw(self):
        #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.setDaemon(True)
        btn_handler.start()

        while True:
            wait_for_press.wait() #waiting for a button to be clicked

            if self.exit_btn.pressed:
                pygame.QUIT
                quit()

            elif self.cont_btn.pressed:
                print(len(self.name.text.split(",")))
                if len(self.name.text.split(",")) <= 4 and len(self.name.text.split(",")) >= 2:
                    self.stop = True
                    return self.name.text.split(",")
                else:
                    animate([255], [0], self.err_anim, [], 120) 

            wait_for_press.clear()
            self.cont_btn.pressed = False
            

    def err_anim(self, start):
        self.show_err = True
        
