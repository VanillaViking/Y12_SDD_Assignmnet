import random
import pygame
from animate import animate


class player():
    def __init__(self, DISPLAY, color):
        self.display = DISPLAY
        self.square = 1
        self.color = color
        self.rolled = 0
        x_ratio = DISPLAY.get_width()/1920 #these are used for displays other than 1080p
        y_ratio = DISPLAY.get_height()/1080

        self.number_coords = [None]
        pos = [int(113 * x_ratio) ,int(975 * y_ratio)] #starting position of pawn
        self.pos = [pos[0],pos[1]] #the actual sprite uses this variable.

        sign = 1

        for num in range(1,101):
            
            self.number_coords.append((pos[0],pos[1]))

            if num % 10 == 0:
               pos[1] =  pos[1] - (int(97 * y_ratio))
               sign *= -1
            else:
                pos[0] = pos[0] + (sign * int(128 * x_ratio))


    def roll(self):
         self.rolled = random.randint(1,6)
         self.square += self.rolled
         return self.rolled

    def check_sl(self):
        
        #is there a better way to do this -_-
        if self.square == 3:
            self.square == 21
            return 'l'

        if self.square == 8:
            self.square == 30
            return 'l'

        if self.square == 17:
            self.square == 13
            return 's'

        if self.square == 28:
            self.square == 84
            return 'l'

        if self.square == 52:
            self.square == 29
            return 's'

        if self.square == 57:
            self.square == 40
            return 's'

        if self.square == 58:
            self.square == 77
            return 'l'

        if self.square == 62:
            self.square == 22
            return 's'

        if self.square == 75:
            self.square == 86
            return 'l'

        if self.square == 80:
            self.square == 100 
            return 'l'

        if self.square == 88:
            self.square == 18
            return 's'

        if self.square == 90:
            self.square == 91
            return 'l'

        if self.square == 95:
            self.square == 51
            return 's'

        if self.square == 97:
            self.square == 79
            return 's'

        if self.square == 100:
            return 'win'

        return 'ok'

    def draw(self):
        pygame.draw.circle(self.display, self.color, self.pos, 20)

    def move(self):
        coords = self.number_coords[self.square]
        temp = [self.pos[0],self.pos[1]]
        animate(temp, coords, self.anim_move, [], 60)

    def anim_move(self, start):
        self.pos = [int(start[0]),int(start[1])]
        self.draw()
        #pygame.display.update((self.pos[0]-20,self.pos[1]-20,self.pos[0]+20,self.pos[1]+20))
        #pygame.display.update()
