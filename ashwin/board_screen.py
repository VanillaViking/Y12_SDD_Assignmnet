import pygame
import threading
from button import *
from animate import animate
import time

class board_screen():
    def __init__(self, DISPLAY):
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)
        
        #board
        self.bord = pygame.image.load("ashwin/board.png")
        self.bord = pygame.transform.scale(self.bord, (1300 * int(self.display.get_width()/1920),970 * int(self.display.get_height()/1080)))
        

        #exit button
        self.exit_btn = button((230,230,230),(180,180,180), DISPLAY.get_width() - 60, 10, 50, 50, "X")
        self.exit_btn.anim = False
       
    def update_btns(self, btn_event):
        while not self.exit_btn.pressed: 
            self.exit_btn.draw(self.display)
            for event in pygame.event.get():
                self.exit_btn.update(event)
            pygame.display.update(self.exit_btn.rect)
        btn_event.set()

    def draw(self):
        self.display.fill((255,255,255))
        self.display.blit(self.bord, (50,50))
        
        pygame.display.update()
               #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        wait_for_press.wait() #waiting for a button to be clicked

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()

   
   

