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
        
        #singleplayer button
        self.sp_btn = button((230,230,230), (180,180,180), (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) - 105, 200,100, "Singleplayer")
        self.sp_btn.anim = False

        self.mp_btn = button((230,230,230), (180,180,180), (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) +5, 200,100, "Multiplayer")
        self.mp_btn.anim = False

        self.display.fill((255,255,255))

    def update_btns(self, btn_event):
        while not self.sp_btn.pressed and not self.exit_btn.pressed and not self.mp_btn.pressed:
            self.exit_btn.draw(self.display)
            self.sp_btn.draw(self.display)
            self.mp_btn.draw(self.display)
            for event in pygame.event.get():
                self.exit_btn.update(event)
                self.sp_btn.update(event)
                self.mp_btn.update(event)
            pygame.display.update([self.exit_btn.rect, self.sp_btn.rect, self.mp_btn.rect])
        btn_event.set()

    def draw(self):
        #displaying the heading
        self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))
        pygame.display.update()

        #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        wait_for_press.wait()

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()
        elif self.sp_btn.pressed:
            return 'sp'
        else: #else multiplayer
            return 'mp'




