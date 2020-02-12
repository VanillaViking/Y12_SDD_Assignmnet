import pygame
import threading

from button import *
from animate import animate

class choose_screen():
    def __init__(self, DISPLAY):
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)

        self.heading = self.font.render("Choose a marker color", True, (0,0,0)) 

        #exit button
        self.exit_btn = button((230,230,230),(180,180,180), DISPLAY.get_width() - 60, 10, 50, 50, "X")
        self.exit_btn.anim = False

        #red_btn        
        self.red_btn = button((255,0,0),(180,0,0), (DISPLAY.get_width()/5) - 100, (DISPLAY.get_height()/2) -50, 200, 100, "")
        self.red_btn.anim = False

        #green_btn
        self.green_btn = button((0,255,0),(0,180,0), (DISPLAY.get_width() * 2/5) - 100, (DISPLAY.get_height()/2) -50, 200, 100, "")
        self.green_btn.anim = False

        #blue_btn
        self.blue_btn = button((0,0,255),(0,0,180), (DISPLAY.get_width() * 3/5) - 100, (DISPLAY.get_height()/2) -50, 200, 100, "")
        self.blue_btn.anim = False

        #purple_btn
        self.purple_btn = button((255,0,255),(180,0,180), (DISPLAY.get_width() * 4/5) - 100, (DISPLAY.get_height()/2) -50, 200, 100, "")
        self.purple_btn.anim = False

    def update_btns(self, btn_event):
        while True:
            self.exit_btn.draw(self.display)
            self.red_btn.draw(self.display)
            self.purple_btn.draw(self.display)
            self.green_btn.draw(self.display)
            self.blue_btn.draw(self.display)
            for event in pygame.event.get():
                self.exit_btn.update(event)
                self.red_btn.update(event)
                self.blue_btn.update(event)
                self.green_btn.update(event)
                self.purple_btn.update(event)

            pygame.display.update([self.exit_btn.rect, self.red_btn.rect, self.blue_btn.rect, self.green_btn.rect, self.purple_btn.rect])

            if self.exit_btn.pressed or self.red_btn.pressed or self.blue_btn.pressed or self.green_btn.pressed or self.purple_btn.pressed:
                btn_event.set()
                break

    def draw(self):
        self.display.fill((255,255,255))
        
        #display heading
        self.display.blit(self.heading, ((self.display.get_width()/2) - (self.heading.get_width() / 2),(self.display.get_height()/4 - (self.heading.get_height()/2)))) 
        pygame.display.update()
        
        #mutlithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        wait_for_press.wait()

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()
        elif self.red_btn.pressed:
            return (255,0,0)
        elif self.blue_btn.pressed:
            return (0,0,255)
        elif self.green_btn.pressed:
            return (0,255,0)
        elif self.purple_btn.pressed:
            return (255,0,255)








