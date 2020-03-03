import random
import pygame
from animate import animate
from button import button
import threading


class player():
    def __init__(self, DISPLAY, name, color, ai=False):
        self.name = name
        self.ai = ai
        self.display = DISPLAY
        self.square = 1
        self.color = color
        self.radius = 20
        self.rolled = 0
        x_ratio = DISPLAY.get_width()/1920 #these are used for displays other than 1080p
        y_ratio = DISPLAY.get_height()/1080

        self.number_coords = [None]
        pos = [int(113 * x_ratio) ,int(975 * y_ratio)] #starting position of pawn
        self.pos = [pos[0],pos[1]] #the actual sprite uses this variable.

        sign = 1

        for num in range(1,101): #creating a grid of coordinates for the pawn to move
            
            self.number_coords.append((pos[0],pos[1]))

            if num % 10 == 0:
               pos[1] =  pos[1] - (int(97 * y_ratio))
               sign *= -1
            else:
                pos[0] = pos[0] + (sign * int(128 * x_ratio))

        self.mine = mine(DISPLAY) #each player gets a mine


    def roll(self):
         self.rolled = random.randint(1,6)
         if (self.rolled + self.square) > 100:
             return (str(self.rolled) + ", Too high")
         self.square += self.rolled
         return str(self.rolled)

    def check_sl(self):
        
        #is there a better way to do this -_-
        if self.square == 3:
            self.square = 21
            return 'l'

        elif self.square == 8:
            self.square = 30
            return 'l'

        elif self.square == 17:
            self.square = 13
            return 's'

        elif self.square == 28:
            self.square = 84
            return 'l'

        elif self.square == 52:
            self.square = 29
            return 's'

        elif self.square == 57:
            self.square = 40
            return 's'

        elif self.square == 58:
            self.square = 77
            return 'l'

        elif self.square == 62:
            self.square = 22
            return 's'

        elif self.square == 75:
            self.square = 86
            return 'l'

        elif self.square == 80:
            self.square = 100 
            return 'l'

        elif self.square == 88:
            self.square = 18
            return 's'

        elif self.square == 90:
            self.square = 91
            return 'l'

        elif self.square == 95:
            self.square = 51
            return 's'

        elif self.square == 97:
            self.square = 79
            return 's'

        elif self.square == 100:
            return 'win'

        else:
            return 'ok'

    def draw(self):
        pygame.draw.circle(self.display, self.color, self.pos,self.radius)

    def move(self):
        coords = self.number_coords[self.square]
        temp = [self.pos[0],self.pos[1]]
        animate(temp, coords, self.anim_move, [], 60)

    def anim_move(self, start):
        self.pos = [int(start[0]),int(start[1])]
        self.draw()
        #pygame.display.update((self.pos[0]-20,self.pos[1]-20,self.pos[0]+20,self.pos[1]+20))
        #pygame.display.update()

    def win_anim(self, start):
        self.radius = int(start[0])
        self.draw()

class mine():
    def __init__(self, DISPLAY):
        self.selecting = False
        self.selected = threading.Event()
        self.selection = None
        self.active = False
        self.display = DISPLAY
        self.pos = None
        self.image = pygame.image.load("ashwin/mine.png")

        x_ratio = DISPLAY.get_width()/1920 #these are used for displays other than 1080p
        y_ratio = DISPLAY.get_height()/1080

        
        self.image = pygame.transform.scale(self.image, (int(100 * x_ratio),int(100 * y_ratio))).convert_alpha()

        self.rect_list = [] * 100

        temp_pos = [50 * self.display.get_width()/1920, 50 * self.display.get_height()/1080]

        '''for n in range(100, 0, -1):
            self.rect_list[n] = pygame.Rect(temp_pos[0], temp_pos[1], temp_pos[0] + (128*x_ratio), temp_pos[1] + (97 * y_ratio))

            temp_pos = [temp_pos[0]+(128*x_ratio), temp_pos[1]]'''

        sign = 1
        for b in range(10):
            for n in range(9):
                self.rect_list.append(pygame.Rect(temp_pos[0], temp_pos[1],(129*x_ratio),(98 * y_ratio)))
                temp_pos = [temp_pos[0]+(sign*130*x_ratio), temp_pos[1]]
                print(temp_pos)
         
            self.rect_list.append(pygame.Rect(temp_pos[0], temp_pos[1],(129*x_ratio),(98 * y_ratio)))
            temp_pos = [temp_pos[0], temp_pos[1] + (97*x_ratio)]
            sign *= -1

        self.rect_list.reverse()
        self.btn_list = [] 
        for n in self.rect_list:
            self.btn_list.append(button([230,230,230, 0],[180,180,180,190],int(n[0]),int(n[1]),int(n[2]),int(n[3]), ""))
            

    def draw_select(self):
        #self.display.blit(self.image, (self.pos))
        #pygame.draw.rect(self.display, (44,23,254), self.rect_list[40])
        for n in self.btn_list:
            n.draw(self.display)
    
    def update(self, event, player_squares):
        for n in self.btn_list:
            n.update(event)
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            for c,n in enumerate(self.btn_list):
                if n.pressed:
                    n.pressed = False

                    if c == 99:
                        return 'no'
                    if c+1 in player_squares:
                        return 'no'

                    self.selection = c
                    self.selected.set()

                    print(c+1)

    def draw_mine(self):
        if self.selection:
            self.display.blit(self.image, (self.rect_list[self.selection][0],self.rect_list[self.selection][1]))

    def detonate(self):
        self.selection = None
