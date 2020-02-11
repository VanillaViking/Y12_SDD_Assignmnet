import random

class player():
    def __init__(self, color):
        self.square = 1
        self.colour = color

    def roll(self):
        self.square += random.randint(1,6)

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

        return 'ok'


