import pygame
import threading
from button import *
from animate import animate
import time

class board_screen():
    def __init__(self, DISPLAY, players):
        self.surfaces = []
        self.player_turn = 0
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)
        self.sfont = pygame.font.SysFont('Arial', 30)
        self.players = players

        self.update_lock = threading.Lock()
        
        #board
        self.bord = pygame.image.load("ashwin/board.png")
        self.bord = pygame.transform.scale(self.bord, (int(1300 * (self.display.get_width()/1920)),int(970 * (self.display.get_height()/1080)))).convert() #multiplying resolution by size of current display compared to a 1080p screen, done so that image can scale down for smaller displays. (please just use a 1080p screen >...<)l
       
        #random button
        self.rand_btn = button((230,230,230),(180,180,180), (DISPLAY.get_width() * 4/5) - 100, (DISPLAY.get_height()/2) - 50, 200, 100, "Roll")
        self.rand_btn.anim = False

        #exit button
        self.exit_btn = button((230,230,230),(180,180,180), DISPLAY.get_width() - 60, 10, 50, 50, "X")
        self.exit_btn.anim = False
       
    def update_screens(self, btn_event):
        while True:
            self.display.fill((255,255,255)) #bg dlet later

            #Game Board
            self.display.blit(self.bord, (int(50 * self.display.get_width()/1920),int(50 * self.display.get_height()/1080)))
           
            #Drawing Buttons
            self.exit_btn.draw(self.display)
            self.rand_btn.draw(self.display)

            #Updating Buttons
            for event in pygame.event.get():
                self.rand_btn.update(event)
                self.exit_btn.update(event)

            #Drawing Surfaces
            for surf in self.surfaces:
                self.display.blit(surf[0], (surf[1],surf[2]))

            #Drawing Player Pawns
            for n in self.players:
                n.draw()

            pygame.display.update()
           
            #Button press checks
            if self.rand_btn.pressed:
                btn_event.set()

            elif self.exit_btn.pressed:
                btn_event.set()
                break


    def draw(self):

        wait_for_press = threading.Event() 

        #screen is updated on separate thread 
        screen_handler = threading.Thread(target=self.update_screens, args=(wait_for_press,))
        screen_handler.start()


        while True:
            wait_for_press.wait() #waiting for a button to be clicked

            if self.exit_btn.pressed:
                pygame.QUIT
                quit()

            elif self.rand_btn.pressed:
                if not self.players[self.player_turn].ai:
                    roll = self.players[self.player_turn].roll()
                    self.say("You rolled " + str(roll), 0.7)
                    self.move_player()

                    self.player_turn += 1
                self.rand_btn.pressed = False

                if self.player_turn == len(self.players):
                    self.player_turn = 0
                
                wait_for_press.clear() #resetting the event
            
            if self.players[self.player_turn].ai:
                self.check_ai(self.players[self.player_turn])


    def move_player(self):
        mover = self.players[self.player_turn]

        temp = [mover.pos[0],mover.pos[1]]
        animate(temp, mover.number_coords[mover.square], self.anim_move, [mover], 60, 0.01)
        time.sleep(0.2)
        if mover.check_sl() != 'ok':
            temp = [mover.pos[0],mover.pos[1]]
            print(mover.square)
            animate(temp, mover.number_coords[mover.square], self.anim_move, [mover], 60, 0.01)

    def anim_move(self, mover, start):
        mover.pos = [int(start[0]),int(start[1])]

    def check_ai(self, player):
        ai_roll = player.roll() 

        self.say(("AI rolled " + str(ai_roll)), 0.6) 
        
        self.move_player()
        self.player_turn += 1
        if self.player_turn == len(self.players):
            self.player_turn = 0

    def say(self, text, tim):
        self.surfaces = []
        thing = self.sfont.render(text, True, (0,0,0))
        self.surfaces.append([thing, (self.display.get_width()*4/5) - thing.get_width()/2, (self.display.get_height()/2) - 110])
        time.sleep(tim)
   

