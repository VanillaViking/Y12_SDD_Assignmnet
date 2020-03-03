import pygame
import threading
from button import *
from animate import animate
import time
import bg

class starting_screen():
    def __init__(self, DISPLAY, bg):
        self.bg = bg
        DISPLAY.fill((0,0,0))

        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)


        
        #weclome text
        self.welcome = self.font.render("Welcome", True, (255,255,255))

        #exit button
        self.exit_btn = button([230,230,230,100],[180,180,180,190], DISPLAY.get_width() - 60, 10, 50, 50, "X")

        #surface to create bg fade illusion
        self.fade_surf = pygame.Surface((self.display.get_width(),self.display.get_height()))
        self.fade_surf.fill((255,255,255))

        #heading
        self.heading = self.font.render("Snakes & Ladders", True, (255,255,255))
        
        #singleplayer button
        self.sp_btn = button([230,230,230,100], [180,180,180,190], (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) - 105, 200,100, "Singleplayer")

        self.mp_btn = button([230,230,230,100], [180,180,180,190], (DISPLAY.get_width()/2) -100, (DISPLAY.get_height() * 3/4) +5, 200,100, "Multiplayer")


    def update_btns(self, btn_event):
        while not self.sp_btn.pressed and not self.exit_btn.pressed and not self.mp_btn.pressed:
            self.bg.draw()

            #heading
            self.display.blit(self.heading, ((self.display.get_width() / 2) - (self.heading.get_width() / 2),(self.display.get_height()/4) - (self.heading.get_height() / 2)))

            self.exit_btn.draw(self.display)
            self.sp_btn.draw(self.display)
            self.mp_btn.draw(self.display)
            for event in pygame.event.get():
                self.exit_btn.update(event)
                self.sp_btn.update(event)
                self.mp_btn.update(event)
            #pygame.display.update([self.exit_btn.rect, self.sp_btn.rect, self.mp_btn.rect])
            pygame.display.update()
        btn_event.set()

    def draw(self):
        #animating welcome

        self.display.blit(self.welcome, ((self.display.get_width() / 2) - (self.welcome.get_width() / 2),(self.display.get_height()/2) - (self.welcome.get_height() / 2)))
        pygame.display.update()

        time.sleep(0.7)
        animate([0,0,0], (255,255,255), self.background_fade, [], 80)


        #animating and displaying the heading
        animate([255], [0], self.anim_heading, [], 80)


        #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        #self.background.anim_start()

        wait_for_press.wait() #waiting for a button to be clicked

        if self.exit_btn.pressed:
            pygame.QUIT
            quit()
        elif self.sp_btn.pressed:
            return 'sp'
        else: #else multiplayer
            return 'mp'

    def anim_heading(self, start):
        self.fade_surf.set_alpha(int(start[0]))

        self.bg.draw()

        self.exit_btn.draw(self.display)
        self.sp_btn.draw(self.display)
        self.mp_btn.draw(self.display)

        self.display.blit(self.fade_surf, (0,0))

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

        

