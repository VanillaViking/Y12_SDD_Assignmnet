import pygame
import threading
from button import *
from animate import animate
import time
import bg

class board_screen():
    def __init__(self, DISPLAY, players):
        self.surfaces = []
        self.player_turn = 0
        self.display = DISPLAY
        self.font = pygame.font.SysFont('Arial', 50)
        self.sfont = pygame.font.SysFont('Arial', 30)
        self.players = players
        self.stop_draw = False
        self.winner = None
        self.kill = False
        self.turn_text = self.sfont.render(self.players[self.player_turn].name + "'s Turn", True, (255,255,255))
        self.bg = bg.scrolling_bg(DISPLAY, (0,45,16), ["ashwin/snek.png","ashwin/ladder.png"], 10, False)
        self.mine_text = self.sfont.render("Mine Acquired! Click to place.", True, (255,255,255)) 
        self.mine_squares = [None] * len(players)

        #board
        self.bord = pygame.image.load("ashwin/board.png")
        self.bord = pygame.transform.scale(self.bord, (int(1300 * (self.display.get_width()/1920)),int(970 * (self.display.get_height()/1080)))).convert_alpha() #multiplying resolution by size of current display compared to a 1080p screen, done so that image can scale down for smaller displays. (please just use a 1080p screen >...<)
       
        #random button
        self.rand_btn = button([230,230,230, 100],[180,180,180,190], (DISPLAY.get_width() * 4/5) - 100, (DISPLAY.get_height()/2) - 50, 200, 100, "Roll")

        #exit button
        self.exit_btn = button([230,230,230, 100],[180,180,180, 190], DISPLAY.get_width() - 60, 10, 50, 50, "X")
      

      
    def update_screens(self, btn_event):
        while not self.kill:
            self.bg.draw()

            #Game Board
            self.display.blit(self.bord, (int(50 * self.display.get_width()/1920),int(50 * self.display.get_height()/1080)))
           
            #Drawing Buttons
            self.exit_btn.draw(self.display)
            self.rand_btn.draw(self.display)

            #Updating Buttons
            for event in pygame.event.get():
                self.rand_btn.update(event)
                self.exit_btn.update(event)
                for n in self.players:
                    if n.mine.selecting:
                        n.mine.update(event, [n.square for n in self.players])

            #Text showing player turn
            self.display.blit(self.turn_text, ((self.display.get_width() *4/5)-(self.turn_text.get_width()/2),(self.display.get_height()/8)-(self.turn_text.get_height()/2))) 

            #Drawing Surfaces
            for surf in self.surfaces:
                self.display.blit(surf[0], (surf[1],surf[2]))

            #Drawing Player Pawns
            if not self.stop_draw:
                for n in self.players:
                    n.draw()
                    n.mine.draw_mine()

                    if n.mine.selecting:
                        n.mine.draw_select()
                        self.display.blit(self.mine_text, ((self.display.get_width() * 4/5) - (self.mine_text.get_width()/2), (self.display.get_height()*3/4) - (self.mine_text.get_height()/3)))

            else:
                self.winner.draw()

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
        screen_handler.setDaemon(True)
        screen_handler.start()
        
        #bg is updated on separate thread
        self.bg.anim_start()

        while not self.winner: #LOGIC LOOP

            wait_for_press.wait() #waiting for a button to be clicked
            if self.exit_btn.pressed:
                pygame.QUIT
                quit()

            elif self.rand_btn.pressed:
                if self.stop_draw:
                    break
                
                #player roll
                self.despawn_mines()
                roll = self.players[self.player_turn].roll()
                self.say(self.players[self.player_turn].name + " rolled " + roll, 0)
                self.move_player()

                if roll == "6":
                    if not self.players[self.player_turn].mine.selection:
                        self.give_mine(self.players[self.player_turn])

                self.player_turn += 1

            if self.player_turn == len(self.players):
                self.player_turn = 0
                wait_for_press.clear() #resetting the event
           
            #changing player turn
            self.turn_text = self.sfont.render(self.players[self.player_turn].name + "'s Turn", True, (255,255,255))
            self.rand_btn.pressed = False

            if self.players[self.player_turn].ai:
                if not self.stop_draw:
                    self.check_ai(self.players[self.player_turn])

            self.check_same_square()
            wait_for_press.clear()
            #print(self.players[0].pos, self.players[1].pos)



    def move_player(self):
        mover = self.players[self.player_turn]
        temp = [mover.pos[0],mover.pos[1]]
        animate(temp, mover.number_coords[mover.square], self.anim_move, [mover], 60, 0.01)
        time.sleep(0.2)
        for c,n in enumerate(self.mine_squares):
            if mover.square == n:
                mover.square = 1

                temp = [mover.pos[0],mover.pos[1]]

                self.players[c].mine.detonate()
                self.mine_squares[c] = None
                animate(temp, mover.number_coords[mover.square], self.anim_move, [mover], 60, 0.01)
                time.sleep(0.2)



        status = mover.check_sl()  #check if mover lands on a snake/ladder

        if status == 'ok':
            return 0

        elif mover.square == 100:
            time.sleep(0.3)
            self.winner = mover 
            self.stop_draw = True
            animate([20], [1800], self.players[self.player_turn].win_anim,[], 80, 0.01)
            #time.sleep(0.5)
            self.kill = True
            return 'win'

        else:
            temp = [mover.pos[0],mover.pos[1]]
            animate(temp, mover.number_coords[mover.square], self.anim_move, [mover], 60, 0.01)



    def anim_move(self, mover, start):
        mover.pos = [int(start[0]),int(start[1])]



    def check_ai(self, player):
        ai_roll = player.roll() 
        self.say(("AI rolled " + str(ai_roll)), 0) 
        self.move_player() 
        self.player_turn += 1

        if self.player_turn == len(self.players):
            self.player_turn = 0

        self.turn_text = self.sfont.render(self.players[self.player_turn].name + "'s Turn", True, (255,255,255))



    def say(self, text, tim):
        self.surfaces = []
        thing = self.sfont.render(text, True, (255,255,255))
        self.surfaces.append([thing, (self.display.get_width()*4/5) - thing.get_width()/2, (self.display.get_height()/2) - 110])
        time.sleep(tim)



    def check_same_square(self):
        for c,n in enumerate(self.players):
            if self.players[c-1].pos == n.pos:
                    temp = [n.pos[0],n.pos[1]]
                    animate(temp, (temp[0],temp[1]+(10)), self.anim_move, [n], 10, 0.01)

                    temp_2 = [self.players[c-1].pos[0],self.players[c-1].pos[1]]
                    animate(temp_2, (temp_2[0],temp_2[1]-(10)), self.anim_move, [self.players[c-1]], 10, 0.01)

        if len(self.players) == 4:
            if self.players[0].pos == self.players[2].pos: #checking this scenario since it does not get checked by the for loop above.
                    temp = [self.players[0].pos[0], self.players[0].pos[1]]
                    animate(temp, (temp[0],temp[1]+10), self.anim_move, [self.players[0]], 10, 0.01)

                    temp_2 = [self.players[2].pos[0],self.players[2].pos[1]]
                    animate(temp_2, (temp_2[0],temp_2[1]-10), self.anim_move, [self.players[2]], 10, 0.01)



    def give_mine(self, plr):
        plr.mine.selecting = True

        plr.mine.selected.wait()  
        
        self.mine_squares[self.player_turn] = plr.mine.selection+1
        print(self.mine_squares)
        plr.mine.selecting = False
        plr.mine.selected.clear()

    def despawn_mines(self):    #detonate any mines that have already been passed by all players 
        for c,n in enumerate(self.mine_squares):
            despawn = True
            if n:
                for p in self.players:
                    if p.square < n:
                        despawn = False
                        break

                if despawn:
                    self.players[c].mine.detonate()
            
            

