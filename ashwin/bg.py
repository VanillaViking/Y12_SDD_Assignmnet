import pygame
import threading
import random
import animate
import time

class scrolling_bg():
    def __init__(self, DISPLAY, bg_color, image_paths, objects):
        self.bg_color = bg_color
        self.images = []
        self.display = DISPLAY
        self.objects_a = [] #[image, [x,y]]
        self.stop = False
        
        for n in image_paths:
            self.images.append(pygame.image.load(n).convert_alpha())
        for n in range(objects):
            self.objects_a.append([random.randint(0,1), [random.randint(50,self.display.get_width() - 50),random.randint(50, self.display.get_height() - 50)]])

    def draw(self):
        self.display.fill(self.bg_color)

        for n in self.objects_a:
            self.display.blit(self.images[n[0]], (n[1][0],n[1][1]))




    def obj_update(self):
            for c,n in enumerate(self.objects_a):
                self.objects_a[c][1][1] -= 1

    def anim_start(self):
        thr_a = threading.Thread(target=self.obj_update)
        thr_a.setDaemon(True)
        thr_a.start()


    def kill(self):
        self.stop = True
        print("kil")
            

        



