import pygame
import sys

#append the folder to system path:
sys.path.append("ashwin/")
sys.path.append("minesweeper/")       # I have doubts about this - S 
sys.path.append("battleships/")
 
#import game file(s):
import snakes_ladders
import battleships
#import minesweeper

import bg


pygame.init()

white = [255,255,255]                   
black = [0,0,0]
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)                                  #full screen display
#window = pygame.display.set_mode((1280, 720))                                  #full screen display
pygame.display.set_caption("BARS launcher")                                                 #setting the name at the title bar
window.fill(white)                                                                          #white background

screen_resolution = pygame.display.Info() 
win_width,win_height = (screen_resolution.current_w, screen_resolution.current_h)           #the length and width of the window

count = 0
bg_x,bg_y,bg_width,bg_height = 0,48,10,10                                                   #variables for making the rocket fly 
rad1,rad2 = win_width,win_height                                                            #radii of the ellipse (the orange curve in the bg in homescreen)

r1,g1,b1 = 255,255,255                                                                      #colours for click to continue
g1_cnt = 1                                                                                  #indicates to either decrease or increase the values for r,g,b 
wait = 0                                                                                    #for avoiding multiple clicks

#snakes and ladders background

def set_img(img_name, img_x, img_y, height, width, opacity):                                #for setting images 
    picture = pygame.image.load(img_name)                                                   #load image
    picture = pygame.transform.scale(picture, (width, height))                              #changing the size of the image
    return picture

def draw_img(picture, img_x, img_y, height, width, opacity):                                               #for drawing the image onto the window

    picture = pygame.transform.scale(picture, (width, height))                              #changing the size of the image
    temp = pygame.Surface((height, width)).convert()                                        #creating a temporary surface

    temp.blit(picture, (0,0))                                                               #setting the image on the surface
    temp.set_alpha(opacity)                                                                 #allowing transparency for the temp surface
    window.blit(temp, (img_x,img_y))                                                        #setting the surface on the window



def text_box(font,font_size,text,R,G,B,x,y):                                                #for creating a text box
    font = pygame.font.SysFont(font, font_size)                                             #set font and define size
    Text = font.render(text, True, [R,G,B])                                                 #rendering font and setting colour
    Text_surface = Text.get_rect()                                                          #provide text with a surface 
    Text_surface.center = (x,y)                                                             #set the position of the center of the surface
    window.blit(Text, Text_surface)                                                         #setting it on the window


rocket = set_img('launcher.png',int(bg_x*win_width/64),int(bg_y*win_height/64),int(bg_width*win_width/64),int(bg_height*win_width/64),255)

black_bg = set_img("black.jpg",0,0,win_width,win_height,120)                                                                           #black background with transparency effect

mine1 = set_img('mine.jpg',int(-5*win_width/64),int(-6*win_height/64),int(14*win_width/64),int(14*win_width/64),255)
mine2 = set_img('mine.jpg',int(11*win_width/64),int(-4*win_height/64),int(9*win_width/64),int(9*win_width/64),255)
mine3 = set_img('mine.jpg',int(22*win_width/64),int(-3*win_height/64),int(6*win_width/64),int(6*win_width/64),255)

mine4 = set_img('mine2.jpg',int(-5*win_width/64),int(-6*win_height/64),int(17*win_width/64),int(17*win_width/64),255)
mine5 = set_img('mine2.jpg',int(13*win_width/64),int(-4*win_height/64),int(11*win_width/64),int(11*win_width/64),255)
mine6 = set_img('mine2.jpg',int(25*win_width/64),int(-3*win_height/64),int(7*win_width/64),int(7*win_width/64),255)

#surface for snakes and ladders bg
bg_surf = pygame.Surface((int(33*win_width/64),int(33*win_height/64)))
bg_surf.fill((255,255,255))

snake_bg = bg.scrolling_bg(bg_surf, (255,255,255), ["ashwin/snek.png","ashwin/ladder.png"], 15)
#snake_bg.stop = True
snake_bg.anim_start()

snek = set_img('snake.jpg', int(45*win_width/64),int(26*win_height/64),300,300,255)
ladder  = set_img('lladder.png', int(45*win_width/64),int(26*win_height/64),300,300,255)

#making a forever loop for making the program to run continuously
prog_running = True     
while prog_running:
    #for exiting the forever loop and stop the program
    for py_event in pygame.event.get():
        if py_event.type == pygame.QUIT:
            prog_running = False

    mouse_press = pygame.mouse.get_pressed()                                            #mouse_press[0] - left button , [1] -  cursor , [2] - right button
    mouse_pos = pygame.mouse.get_pos()                                                  #mouse_pos[0] - x coordinate, [1] - y coordinate
    pygame.display.flip()                                                               #updating the screen


#------------------------------------------------------------------------------------homescreen----------------------------------------------------------------------------------


    if count == 0:
        text_box('lucidacalligraphy',int(2*win_height/64),"name of the launcher",0,0,0,int(10*win_width/64),int(7*win_height/64))               #title of the launcher (increase size appropriately)
        if bg_y > 1:                                                                                                                            #for rocket animation
            pygame.draw.rect(window,white,pygame.Rect(0,0,win_width,win_height),0)
            bg_x += 0.9
            bg_y -= 1
            bg_width += 0.2
            bg_height += 0.2
            draw_img(rocket, int(bg_x*win_width/64),int(bg_y*win_height/64),int(bg_width*win_width/64),int(bg_height*win_width/64),255)

        else:
            draw_img(rocket, int(bg_x*win_width/64),int(bg_y*win_height/64),int(bg_width*win_width/64),int(bg_height*win_width/64),255) #final pos

            if g1_cnt == 1:                                                                                                                     #changing the colour of click to continue text continuously
                g1 -= 15
                r1 -= 15
                b1 -= 15
                if g1 == 0:
                    g1_cnt = 0

            if g1_cnt == 0:                 
                g1 += 15
                r1 += 15
                b1 += 15
                if g1 == 255:
                    g1_cnt = 1
            text_box('times new roman',int(5*win_height/64),"CLICK TO CONTINUE",r1,g1,b1,int(16*win_width/64),int(36*win_height/64))

            if mouse_press[0] == 1:                                                                                                             #click to go to the select game screen
                count = 1
        
        if rad1 < 2.5*win_width:                                                                                                                #ellipse animation
            rad1 += win_width/32
        if rad2 < 2.5*win_height:
            rad2 += win_height/32
        pygame.draw.ellipse(window,(255,64,0),[-win_width,-win_height,int(rad1),int(rad2)],int(rad2/2))

#---------------------------------------------------------------------------------gameselectscreen-------------------------------------------------------------------------------------
        
    elif count == 1:
        draw_img(black_bg, 0,0,win_width,win_height, 120)
        pygame.draw.line(window,white,(int(win_width/2),0),(int(win_width/2),win_height),4)                                                   #dividing the screen in 4 parts
        pygame.draw.line(window,white,(0,int(win_height/2)),(win_width,int(win_height/2)),4)
        wait += 1


        '''
            FORMAT FOR THE CODE OF EACH GAME
            game name
            set an image related to your game or if ashwin wants the parallax effect   
            if mouse hovered over your game's section, change the background of that part to white, increase font size and the background image
            if mouse clicked call the function which launches your game and then reset the variables to default
        '''
        


        #minesweeper
        text_box('lucidacalligraphy',int(3*win_height/64),"Minesweeper",255,255,255,int(24*win_width/64),int(27*win_height/64))
        
        draw_img(mine1, int(-5*win_width/64),int(-6*win_height/64),int(14*win_width/64),int(14*win_width/64), 255)
        draw_img(mine2, int(11*win_width/64),int(-4*win_height/64),int(9*win_width/64),int(9*win_width/64),255)
        draw_img(mine3, int(22*win_width/64),int(-3*win_height/64),int(6*win_width/64),int(6*win_width/64),255)



        if pygame.Rect(0,0,int(32*win_width/64),int(32*win_height/64)).collidepoint(mouse_pos[0],mouse_pos[1]):
            pygame.draw.rect(window,white,pygame.Rect(0,0,int(33*win_width/64),int(33*win_height/64)),0)
            text_box('lucidacalligraphy',int(4.5*win_height/64),"Minesweeper",0,0,0,int(22*win_width/64),int(26*win_height/64))

            draw_img(mine4,int(-5*win_width/64),int(-6*win_height/64),int(17*win_width/64),int(17*win_width/64),255)
            draw_img(mine5,int(13*win_width/64),int(-4*win_height/64),int(11*win_width/64),int(11*win_width/64),255)
            draw_img(mine6,int(25*win_width/64),int(-3*win_height/64),int(7*win_width/64),int(7*win_width/64),255)



            
            '''if mouse_press[0] == 1 and wait >= 15:
                __name__ = '__ms__'
                minesweeper.minesweeper_game()
                count = 0
                wait = 0'''     #this works but I disabled it for now cauz you would need my game and all the related files as well



        #battle
        text_box('lucidacalligraphy',int(3*win_height/64),"BattleShip",255,255,255,int(39*win_width/64),int(36*win_height/64))
        
        if pygame.Rect(int(32*win_width/64),int(32*win_height/64),int(32*win_width/64),int(32*win_height/64)).collidepoint(mouse_pos[0],mouse_pos[1]):
            pygame.draw.rect(window,white,pygame.Rect(int(31*win_width/64),int(31*win_height/64),int(33*win_width/64),int(33*win_height/64)),0)
            text_box('lucidacalligraphy',int(4.5*win_height/64),"BattleShip",0,0,0,int(40*win_width/64),int(37*win_height/64))

        if mouse_press[0] == 1 and wait >= 15:
            __name__ = '__bs__' 
            battleships.Battleships(window)
            count = 0
            wait = 0


            
        #memory
        text_box('lucidacalligraphy',int(3*win_height/64),"Memory Game",255,255,255,int(23*win_width/64),int(36*win_height/64))
        
        if pygame.Rect(0,int(32*win_height/64),int(32*win_width/64),int(32*win_height/64)).collidepoint(mouse_pos[0],mouse_pos[1]):
            pygame.draw.rect(window,white,pygame.Rect(0,int(31*win_height/64),int(33*win_width/64),int(33*win_height/64)),0)
            text_box('lucidacalligraphy',int(4.5*win_height/64),"Memory Game",0,0,0,int(21*win_width/64),int(37*win_height/64))


        #snakes
        text_box('lucidacalligraphy',int(3*win_height/64),"Snakes & Ladders",255,255,255,int(42*win_width/64),int(27*win_height/64))

        draw_img(snek, int(45*win_width/64)-200,int(26*win_height/64)-200,200,200,255)
        draw_img(ladder, int(45*win_width/64),int(8.2*win_height/64),200,200,255)

        if pygame.Rect(int(32*win_width/64),0,int(32*win_width/64),int(32*win_height/64)).collidepoint(mouse_pos[0],mouse_pos[1]):
            window.blit(bg_surf, (int(31*win_width/64),0))
            #pygame.draw.rect(window,white,pygame.Rect(int(31*win_width/64),0,int(33*win_width/64),int(33*win_height/64)),0)
            text_box('lucidacalligraphy',int(4.5*win_height/64),"Snakes & Ladders",0,0,0,int(45*win_width/64),int(26*win_height/64))
            snake_bg.stop = False
            snake_bg.draw()

            if mouse_press[0] == 1 and wait >= 15:
                __name__ = '__sl__'
                snakes_ladders.run(window)
                count = 0
                wait = 0


