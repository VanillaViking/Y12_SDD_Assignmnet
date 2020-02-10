import pygame
import threading
from button import *
from text_input import *


class starting_screen():
    def __init__(self, DISPLAY):
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)

        #exit button
        self.exit_btn = button((230,230,230),(180,180,180), DISPLAY.get_width() - 60, 10, 50, 50, "X")
        self.exit_btn.anim = False

        #heading
        self.heading = self.font.render("Snakes & Ladders", True, (0,0,0))
        
        #continue button
        self.cont_button = button((230,230,230), (180,180,180), (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) - 50, 200,100, "Continue")
        self.cont_button.anim = False

        self.display.fill((255,255,255))

    def update_btns(self, btn):
        while not self.cont_button.pressed and not self.exit_btn.pressed:
            btn.draw(self.display)
            for event in pygame.event.get():
                btn.update(event)
            pygame.display.update(btn.rect)

    def draw(self):
        #displaying the heading
        self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))
        pygame.display.update()
        #multithreading the buttons

        exit_handler = threading.Thread(target=self.update_btns, args=(self.exit_btn,))
        exit_handler.start()

        cont_handler = threading.Thread(target=self.update_btns, args=(self.cont_button,))
        cont_handler.start()
            
          


    





