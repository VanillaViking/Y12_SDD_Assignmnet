import pygame
import threading
from button import *
from animate import animate
import time

class board_screen():
    def __init__(self, DISPLAY, players):
        self.player_turn = 0
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)
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
       
    def update_btns(self, btn_event):
        while not self.exit_btn.pressed: 
            
            self.display.blit(self.bord, (int(50 * self.display.get_width()/1920),int(50 * self.display.get_height()/1080)))
            
            self.exit_btn.draw(self.display)
            self.rand_btn.draw(self.display)
            for event in pygame.event.get():
                self.rand_btn.update(event)
                self.exit_btn.update(event)
            for n in self.players:
                n.draw()
            #if not self.update_lock.locked():
                #pygame.display.update([self.exit_btn.rect, self.rand_btn.rect])
            pygame.display.update()
            
            if self.rand_btn.pressed:
                btn_event.set()
        btn_event.set()

    def update_board(self):
        while not self.exit_btn.pressed:
            self.display.blit(self.bord, (int(50 * self.display.get_width()/1920),int(50 * self.display.get_height()/1080)))

            for n in self.players:
                n.draw()


    def draw(self):
        self.display.fill((255,255,255))
        self.display.blit(self.bord, (int(50 * self.display.get_width()/1920),int(50 * self.display.get_height()/1080)))
        for each in self.players:
            each.draw()
        
        pygame.display.update()
               #multithreading the buttons
        wait_for_press = threading.Event()

        btn_handler = threading.Thread(target=self.update_btns, args=(wait_for_press,))
        btn_handler.start()

        board_handler = threading.Thread(target=self.update_board)
        #board_handler.run()

        while True:
            if self.update_lock.locked():
                self.update_lock.release()
            wait_for_press.wait() #waiting for a button to be clicked

            if self.exit_btn.pressed:
                pygame.QUIT
                quit()

            elif self.rand_btn.pressed:
                self.players[self.player_turn].roll()
                self.move_player()
                self.player_turn += 1
                self.rand_btn.pressed = False

                if self.player_turn == len(self.players):
                    self.player_turn = 0
                
                wait_for_press.clear()

    def move_player(self):
        mover = self.players[self.player_turn]
        coords = mover.number_coords[mover.square]
        print(mover.square, coords)
        temp = [mover.pos[0],mover.pos[1]]
        self.update_lock.acquire()
        animate(temp, coords, self.anim_move, [mover], 60, 0.01)

    def anim_move(self, mover, start):
        mover.pos = [int(start[0]),int(start[1])]

        #self.display.blit(self.bord, (int(50 * self.display.get_width()/1920),int(50 * self.display.get_height()/1080)))

        #mover.draw()
        #pygame.display.update()

   
   

