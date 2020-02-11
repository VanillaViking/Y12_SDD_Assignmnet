import pygame
import threading
from button import *
from animate import animate
import time

class starting_screen():
    def __init__(self, DISPLAY):
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)

        #weclome text
        self.welcome = self.font.render("Welcome", True, (255,255,255))

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
        #animating welcome

        self.display.blit(self.welcome, ((self.display.get_width() / 2) - (self.welcome.get_width() / 2),(self.display.get_height()/2) - (self.welcome.get_height() / 2)))
        pygame.display.update()

        time.sleep(0.7)
        animate([0,0,0], (255,255,255), self.background_fade, [], 50)


        #animating and displaying the heading
        animate([255,255,255], (0,0,0), self.anim_heading, [], 20, 0.02)

        time.sleep(0.4)
        self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))
        pygame.display.update()

        #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        wait_for_press.wait() #waiting for a button to be clicked

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()
        elif self.sp_btn.pressed:
            return 'sp'
        else: #else multiplayer
            return 'mp'

    def anim_heading(self, start):
        self.heading = self.font.render("Snakes & Ladders", True, (start[0],start[1],start[2]))

        self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))
        pygame.display.update()
    
    def welcome_entry(self, start):
        self.welcome = self.font.render("Welcome", True, (start[0],start[1],start[2]))

        self.display.blit(self.welcome, ((self.display.get_width() / 2) - (self.welcome.get_width() / 2),(self.display.get_height()/2) - (self.welcome.get_height() / 2)))
        pygame.display.update()
    
    def background_fade(self, start):
        self.display.fill(start)

        self.display.blit(self.welcome, ((self.display.get_width() / 2) - (self.welcome.get_width() / 2),(self.display.get_height()/2) - (self.welcome.get_height() / 2)))
        pygame.display.update()

