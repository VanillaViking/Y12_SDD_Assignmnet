import pygame,time,random
pygame.init()
 
def Battleships(Display): #main game code
    # Window Parameters
    info = pygame.display.Info()# current_w = 1366, current_h = 768 for my computer
    display_width = info.current_w
    display_height = info.current_h
    #Display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Battleship') #Window title

    # Colour variables
    black = 0,0,0
    white = 255,255,255
    red = 255,0,0
    green = 0,255,0
    blue = 0,0,255
    light_blue = 16,61,110
    neon_blue = 0,100,255
    coffee = 163, 118, 54
    grey = 100,100,100
    dark_red = 161,0,0

    crashed = False
    screen = 0
    ship_mov_count = display_width
    font0 = pygame.font.Font("battleships/warfont.otf",500)
    text0 = font0.render("Battleships", True,coffee) #text, ,RGB





    # Image imports
    fleet_img = pygame.image.load("battleships/fleet.png") #1600 x 654
    ship1 = pygame.image.load("battleships/Untitled-11.png") #621*403
    ship2 = pygame.image.load("battleships/Untitled-10.png") #618*188
    homebutton = pygame.image.load("battleships/Homebutton.png") #512*512
    torpedo = pygame.image.load("battleships/torpedo.png") #199*1027

    # Image transforms
    fleet_img_tr1 = pygame.transform.scale(fleet_img,(display_width, display_height))
    ship1_tr = pygame.transform.scale(ship1,(300, 200))
    homebutton_tr = pygame.transform.scale(homebutton,(50, 50))
    torpedo_tr = pygame.transform.scale(torpedo,(50, 150)) 
    # Functions

    def button(display,colour,x_pos,y_pos,button_width,button_height,thickness): #basic button
        mousebutton = pygame.mouse.get_pressed() #event for mouse clicks
        mouse_pos = pygame.mouse.get_pos() #pointer position
        pygame.draw.rect(display,(0,0,0),(x_pos,y_pos,button_width,button_height)) #draws rectangle with a black background for button base
        if x_pos<mouse_pos[0]<(x_pos+button_width)and y_pos<mouse_pos[1]<(y_pos+button_height): # if pointer is in the button parameter then
            pygame.draw.rect(display,colour,(x_pos,y_pos,button_width,button_height),thickness) # another rectangle is drawn but only the perimeter is coloured
        if mousebutton[0] == 1 and x_pos<mouse_pos[0]<(x_pos+button_width)and y_pos<mouse_pos[1]<(y_pos+button_height): # if mouse click occurs then True is returned 
            time.sleep(0.1)
            return True
        
    def text(display,colour1,x_pos,y_pos,text_width,text_height,font,font_size,texts): #basic text function to display text
        mouse_pos = pygame.mouse.get_pos() #pointer position
        if x_pos<mouse_pos[0]<(x_pos+text_width)and y_pos<mouse_pos[1]<(y_pos+text_height): #changes text colour if pointer in parameter
            colour = colour1
            #pygame.draw.rect(display,colour,(x_pos,y_pos,text_width,text_height),2)
        else:
            colour = white
        font = pygame.font.Font(font, font_size)
        text = font.render(str(texts), True,colour) #text, ,RGB
        display.blit(text,(x_pos,y_pos))

    class AI:
        def __init__(self):
            self.xy = []
            self.check_grid = []
            
            self.aim = []
            self.hit = []
            self.overlapcheck = []
            self.hit_check = [0] #1 = hit, 0 = miss
        def AI_grid(self):
            check_grid = []
            count0 = 0
            while count0 <= 2:
                x = random.randint(0,setup.size)
                y = random.randint(0,setup.size)
                if (str(x),str(y)) in self.check_grid or y in self.overlapcheck:
                    check0 = False
                else:
                    check0 = True
                    self.overlapcheck.append(y)
                    count0 +=1
                self.check_grid.append((str(x),str(y)))
                xpos = x*setup.box_width + x
                ypos = y*setup.box_height + y
                count = 0

                while count <= 2 and check0 == True:
                    #pygame.draw.rect(Display,(255,100,100),(xpos,ypos,user.box_width,user.box_height),0)
                    #pygame.display.update()
                    self.xy.append((str(xpos),str(ypos)))
                    if x > (setup.size-3):
                        xpos -= (setup.box_width +1)
                    else:
                        xpos += setup.box_width +1
                    count +=1
                    
        def AI_main(self,call): #check if to find errors and debug the program
            while call == True:
                if self.hit_check[-1] == 0 : #if the last aim was not a hit the function will chose a randm number
                    #print("check 0")
                    x = (random.randint(0,setup.size)*(setup.box_width+1)) #the number will be between 0 to grid size
                    y =(random.randint(0,setup.size)*(setup.box_height+1))
                    if (str(x),str(y)) in self.aim: # checks if the coordinate is previously selected 
                        #print("check 1")
                        call = True # if it is it will run the loop again and select a new set of numbers
                    else:
                        #print("check 2")
                        call = False #if the coordinate is not in the array  
                        self.aim.append((str(x),str(y)))
                        if (str(x),str(y)) in setup.click_checker:
                            #print("check 3")
                            self.hit.append(x)
                            self.hit.append(y)
                            self.hit_check.append(1)
                elif self.hit_check[-1] == 1:
                    #print("check 4")
                    x = (self.hit[-2] + (setup.box_width +1))
                    y = self.hit[-1]
                    if (str(x),str(y)) in self.aim or x > ((setup.size)*(setup.box_width+1)):
                        #print("check 5")
                        call = True
                        self.hit_check.append(2)
                    else:
                        #print("check 6")
                        call = False
                        self.aim.append((str(x),str(y)))
                        if (str(x),str(y)) in setup.click_checker:
                            #print("check 7")
                            self.hit.append(x)
                            self.hit.append(y)
                            self.hit_check.append(1)
                            if (self.hit_check[-3:] == [1,1,1]):
                                #print("check 8")
                                self.hit_check.append(0)
                        else:
                            #print("check 9")
                            self.hit_check.append(2)

                elif self.hit_check[-1] == 2:
                    #print("check 10")
                    x = (self.hit[-2] - (setup.box_width +1))
                    y = self.hit[-1]
                    if self.hit_check[-3:] == [1,1,2] and (str(x),str(y)) in self.aim: 
                        #print("check 11")
                        call = False
                        x =(self.hit[-4] - (setup.box_width +1))
                        if (str(x),str(y)) in setup.click_checker:
                            self.hit.append(x)
                            self.hit.append(y)
                        self.hit_check.append(0)
                    elif (str(x),str(y)) in self.aim or x < 0:
                        #print("check 12")
                        call = True
                        self.hit_check.append(0)
                    else:
                        #print("check 13")
                        call = False
                        self.aim.append((str(x),str(y)))
                        if (str(x),str(y)) in setup.click_checker:
                            #print("check 14")
                            self.hit.append(x)
                            self.hit.append(y)
                            self.hit_check.append(2)
                            if (self.hit_check[-3:] == [2,2,2]):
                                #print("check 15")
                                self.hit_check.append(0)

                                   
                if call == False:
                    #print("check 16")
                    pygame.draw.rect(Display,(grey),(x+setup.start_xpos,y+setup.start_ypos,user.box_width,user.box_height),0)
                    pygame.display.update(x+setup.start_xpos,y+setup.start_ypos,user.box_width,user.box_height)


    # Class         ######################################################################################################################################################

    class player:
        def __init__(self,display,start_xpos,start_ypos,colour,box_width,box_height,size):
            self.display = display
            self.start_xpos = start_xpos
            self.start_ypos = start_ypos
            self.colour = colour
            self.box_width = box_width
            self.box_height = box_height
            self.size = size - 1
            self.display_width = info.current_w
            self.display_height = info.current_h
            self.startposy = []
            self.startposx = []
            self.call = 0
            self.oldstart_xpos = start_xpos
            self.oldstart_ypos = start_ypos


            self.clicked = []
            self.click_checker = []
        def grid(self):
            count = 0 #loop counter
            ycount = 0 # outer ycoordinate loop counter
            while ycount <= self.size: #yloop 
                while count <= self.size: #loop
                    if count < 1: #start position
                        xpos = self.start_xpos
                        if ycount == 0:
                            ypos = self.start_ypos
                        else:
                            ypos = self.start_ypos + (ycount*(self.box_height+1)) #equation for yposition 
                    if count >= 1:
                        xpos = (xpos + (self.box_width+1))
                        ypos = (ypos)
                    if ycount == 0:
                        self.startposx.append(xpos) #appends starting x position of the individual square

                    
                    #print(xpos,ypos)
                    pygame.draw.rect(self.display,self.colour,(xpos,ypos,self.box_width,self.box_height),0) #draws squares left to right up to down
                    #pygame.display.update()
                    count +=1
                count = 0
                self.startposy.append(ypos) #appends starting y position of the individual square
                ycount +=1
            self.call+=1
            for x_letter in range(self.size+1):
                x_letter_pos = x_letter*self.box_width + (self.box_width/2+1) + self.start_xpos
                y_letter_pos = self.start_ypos - 15
                text(Display,coffee,x_letter_pos-2,y_letter_pos,10,10,"battleships/ARLRDBD.TTF",10,x_letter+1)
            for y_letter in range(self.size+1):
                y_letter_pos = y_letter*self.box_height + (self.box_height/2+1) + self.start_ypos
                x_letter_pos = self.start_xpos - 15
                text(Display,coffee,x_letter_pos-2,y_letter_pos,10,10,"battleships/ARLRDBD.TTF",10,y_letter+1)
            pygame.display.update()
            #print("start positions", self.startpos)
            
        def detect(self,selector,click_counter,test): # function to identify mouse click and save the square address
            mouse_pos = pygame.mouse.get_pos()
            mousebutton = pygame.mouse.get_pressed()
            if len(self.clicked) == (2*((self.size+1)**2)):
                return False
            elif self.call >=2 and test == True: #if detect() is called the second time for the same object it reopens the old grid
                for cor in enumerate(self.clicked, start = 0):
                    if cor[0]%2 == 0:
                        xpos = cor[1] - self.oldstart_xpos + self.start_xpos
                    else:
                        ypos = cor[1] - self.oldstart_ypos + self.start_ypos #NOTE NEED TO CHANGE STATIC NUMBERS TO VARIABLES Depending on the placement of the second grid
                        pygame.draw.rect(self.display,(dark_red),(xpos,ypos,self.box_width,self.box_height),0)
                
                
            for x in self.startposx:
                for y in self.startposy:
                    #pygame.draw.line(self.display, (0,0,0), (0,mouse_pos[1]), (self.display_width,mouse_pos[1]), 5) a idea for cross bar
                    if x<mouse_pos[0]<(x+self.box_width) and y<mouse_pos[1]<(y+self.box_height) and mousebutton[0] == 1 and ((str(x-self.start_xpos),str(y-self.start_ypos)) not in self.click_checker): #xposition and yposition are checked with respect to the grid and also checks the mouse position
                        if selector == 1 and click_counter >= 1:
                            if ((self.clicked[-2]-self.box_width-1)<mouse_pos[0]<(self.clicked[-2]-1) and self.clicked[-1]<mouse_pos[1]<(self.clicked[-1]+self.box_height)) or ((self.clicked[-2]+self.box_width+1)<mouse_pos[0]<(self.clicked[-2]+2*(self.box_width)+1) and self.clicked[-1]<mouse_pos[1]<(self.clicked[-1]+self.box_height)):
                                time.sleep(0.1) #sleep function to avoid double click errors
                                pygame.draw.rect(self.display,(neon_blue),(x,y,self.box_width,self.box_height),0) #changes colour for the selected square
                                self.clicked.append(x) #saves the xcoordinate first
                                self.clicked.append(y) #saves the y coordinate in the same list
                                self.click_checker.append((str(x-self.start_xpos),str(y-self.start_ypos))) #saves the relative x,y position of the square
                                pygame.display.update()
                                time.sleep(0.2)
                                return True

                        else:
                            time.sleep(0.1) #sleep function to avoid double click errors
                            pygame.draw.rect(self.display,(neon_blue),(x,y,self.box_width,self.box_height),0) #changes colour for the selected square
                            self.clicked.append(x) #saves the xcoordinate first
                            self.clicked.append(y) #saves the y coordinate in the same list
                            self.click_checker.append((str(x-self.start_xpos),str(y-self.start_ypos)))
                            pygame.display.update()
                            return True
        


    ######################################################################################################################################################################
    ######################################################################################################################################################################


    while not crashed: # Main loop

        for event in pygame.event.get(): # Exit event. If program is closed all other processes will stop
            if event.type == pygame.QUIT:
                crashed = True
  
    ##########################

        if screen == 0:
            ship_mov_count -=2 # this should be -=2 (changes depending on the computer)
            Display.fill(black)
            Display.blit(ship2,(ship_mov_count,int((display_height/2)-(188/2))))
            Display.blit(text0,(ship_mov_count+700,int((display_height/2)-(500/2))))
            if ship_mov_count < -4400:
                screen = 0.5
                selection = [] # General Variable

        elif screen == 0.5:
            Display.blit(fleet_img_tr1,(0,0))

            text(Display,coffee,int(display_width/2 - 350),10,740,80,"battleships/warfont.otf",100,"Battleships") #width of the title is 700
            
            if button(Display,coffee,int(display_width/2 - 90), (int(display_height/2)),180,80,2) == True:
                screen = 1
            text(Display,coffee,int(display_width/2 - 90), (int(display_height/2)),180,80,"battleships/ARLRDBD.TTF",70,"Start")
            
            if button(Display,coffee,int(display_width/2 - 120), (display_height-150),240,75,2) == True:
                __name__ = '__launcher__'
            text(Display,coffee,int(display_width/2 - 120), (display_height-150),240,75,"battleships/ARLRDBD.TTF",60,"B.A.R.S.")

            if button(Display,coffee,int(display_width-60), (10),25,45,2) == True:
                pygame.quit()
            text(Display,coffee,int(display_width- 60), (10),25,45,"battleships/ARLRDBD.TTF",40,"X")
            
    ##########################

        elif screen == 1:
            while screen == 1:
                Display.fill(black)
                setup = player(Display,int(display_width/4)*3-205,100,light_blue,40,40,10)
                setup.grid()
                colour1_indicator = green
                colour2_indicator = green
                colour3_indicator = green
                screen = 2

    ##########################

        elif screen == 2:
            Display.fill(black,pygame.Rect(0,0,int(display_width/2+110),display_height))
            Display.fill(black,pygame.Rect((int(display_width/4)*3-72,510,145,41)))
            
            text(Display,coffee,(int(display_width/2-105)),(10),210,50,"battleships/warfont.otf",60,"setup")
            text(Display,coffee,int(display_width/4)-20,100,90,40,"battleships/ARLRDBD.TTF",30,"Ships")
            text(Display,coffee,int(display_width/4)-100,520,150,20,"battleships/ARLRDBD.TTF",20,"Instructions:")
            text(Display,coffee,int(display_width/4)*3-70,510,140,40,"battleships/ARLRDBD.TTF",30,"Your Grid")

            #pygame.display.flip()

            if button(Display,coffee,int(display_width/4)-100,200,200,25,2) == True and 1 not in selection :
                selection.append(1)
                selection_1 = 3
                screen = 3
                colour1_indicator = red
            text(Display,coffee,int(display_width/4)-98,(200),200,20,"battleships/ARLRDBD.TTF",20,"1: A ship that is 1 * 3")
            pygame.draw.line(Display, colour1_indicator,((int(display_width/4)+112),210),((int(display_width/4)+142),210),10)

            if button(Display,coffee,int(display_width/4)-100,230,200,25,2) == True and 2 not in selection:
                selection.append(2)
                selection_1 = 3
                screen = 3
                colour2_indicator = red
            text(Display,coffee,int(display_width/4)-98,(230),200,20,"battleships/ARLRDBD.TTF",20,"2: A ship that is 1 * 3")
            pygame.draw.line(Display, colour2_indicator,((int(display_width/4)+112),240),((int(display_width/4)+142),240),10)

            if button(Display,coffee,int(display_width/4)-100,260,200,25,2) == True and 3 not in selection:
                selection.append(3)
                selection_1 = 3
                screen = 3
                colour3_indicator = red
            text(Display,coffee,int(display_width/4)-98,(260),200,20,"battleships/ARLRDBD.TTF",20,"3: A ship that is 1 * 3")
            pygame.draw.line(Display, colour3_indicator, ((int(display_width/4)+112),270),((int(display_width/4)+142),270),10)

            if button(Display,coffee,10,10,50,50,2) == True:
                screen = 0
            Display.blit(homebutton_tr,(10,10))

            
            if screen == 2:
                setupins = "Please select a Ship"
                pygame.draw.rect(Display,white,(int(display_width/4)-110,100,260,190),2)# ship selection outline
                pygame.draw.rect(Display,coffee,(int(display_width/4)-110,510,400,100),2)# instruction box outline
            if screen == 3:
                if len(selection) == 3:
                    setupins = "Please place your Ship on 'Your Grid'and press 'Attack'"
                    pygame.draw.rect(Display,coffee,(int(display_width/4)-110,510,560,100),2)# instruction box outline
                    pygame.draw.rect(Display,white,(int(display_width/4)*3-72,510,142,40),2)# Your grid outline
                else:
                    setupins = "Please place your Ship on 'Your Grid'"
                    pygame.draw.rect(Display,coffee,(int(display_width/4)-110,510,400,100),2)# instruction box outline
                    pygame.draw.rect(Display,white,(int(display_width/4)*3-72,510,142,40),2)# Your grid outline
            text(Display,coffee,int(display_width/4)-100,540,250,20,"battleships/ARLRDBD.TTF",20,setupins)
            click_counter = 0

    ##########################

        elif screen == 3:
            
            if button(Display,coffee,10,10,50,50,2) == True:
                screen = 0
            Display.blit(homebutton_tr,(10,10))
            
            if click_counter < selection_1:
                if setup.detect(1,click_counter,False) == True:
                    click_counter += 1
            if click_counter == selection_1:
                if len(selection) == 3:
                    Display.fill(black,pygame.Rect(display_width - 257, (display_height-172),140,55))
                    if button(Display,coffee,(display_width - 255), (display_height-170),135,50,2) == True:
                        screen = 3.5
                    text(Display,coffee,(display_width - 250), (display_height-170),135,50,"battleships/ARLRDBD.TTF",40,"Attack")
                else:
                    screen = 2

    ##########################
        elif screen == 3.5:
            for count in range(5):
                Display.fill(black)
                pygame.display.flip()
                torpedo_mov = display_height
                x_torpedo_mov = random.randint(50,display_width-50)
                while torpedo_mov > -150:
                    Display.blit(torpedo_tr,(int(x_torpedo_mov),int(torpedo_mov)))
                    Display.fill(black,pygame.Rect(int(x_torpedo_mov),int(torpedo_mov)+150,50,10))
                    torpedo_mov -= 0.25
                    pygame.display.update(pygame.Rect(int(x_torpedo_mov),int(torpedo_mov),50,160))
            screen = 4
                

    #########################
        elif screen == 4:
            torpedo_mov = 0
            Display.fill(black)
            text(Display,coffee,(int(display_width/2-160)),(10),320,50,"battleships/warfont.otf",60,"War Zone")
            
            user = player(Display,int(display_width/4)*3-205,100,light_blue,40,40,10)
            user.grid()
            text(Display,coffee,int(display_width/4)*3-150,(525),200,20,"battleships/ARLRDBD.TTF",40,"Opponents Grid")
            
            screen = 5
            screen5_counter = 0
            turn_counter = 0
            
            text(Display,coffee,int(display_width/4)-100,(525),200,20,"battleships/ARLRDBD.TTF",40,"Your Grid")
            setup.start_xpos = int(display_width/4)-205
            setup.start_ypos = 100
            setup.grid()
            setup.detect(0,0,True)
            
            ai = AI()
            ai.AI_grid()

            pygame.draw.rect(Display,(red),(int(display_width/4)-205,625,user.box_width/2,user.box_height/2),0)
            text(Display,coffee,int(display_width/4)-175,625,200,20,"battleships/ARLRDBD.TTF",20,"Red = you hit your opponent's ship")
            
            pygame.draw.rect(Display,(neon_blue),(int(display_width/4)-205,650,user.box_width/2,user.box_height/2),0)
            text(Display,coffee,int(display_width/4)-175,650,200,20,"battleships/ARLRDBD.TTF",20,"Neon blue = coordinates you aimed")
            
            pygame.draw.rect(Display,(dark_red),(int(display_width/4)-205,675,user.box_width/2,user.box_height/2),0)
            text(Display,coffee,int(display_width/4)-175,675,200,20,"battleships/ARLRDBD.TTF",20,"Dark red = your ship arrangement")
            
            pygame.draw.rect(Display,(grey),(int(display_width/4)-205,700,user.box_width/2,user.box_height/2),0)
            text(Display,coffee,int(display_width/4)-175,700,200,20,"battleships/ARLRDBD.TTF",20,"Grey = coordinates your opponent aimed")
            
            pygame.draw.rect(Display,coffee,(int(display_width/4)-215,615,450,115),2)

            pygame.display.flip()


    ##########################

        elif screen == 5:
            
            if turn_counter%2 == 0 and len(ai.hit) < 18:
                Display.fill(black,pygame.Rect(int(display_width/4)*3-210,625,500,50))
                if button(Display,coffee,10,10,50,50,2) == True:
                    screen = 0
                Display.blit(homebutton_tr,(10,10))
                pygame.draw.rect(Display,coffee,(int(display_width/4)*3-215,615,500,50),2)
                text(Display,coffee,int(display_width/4)*3-210,615,150,20,"battleships/ARLRDBD.TTF",20,"Instructions:")
                text(Display,coffee,int(display_width/4)*3-210,635,150,20,"battleships/ARLRDBD.TTF",20,"Your Turn: Please select a coordinate for attack")
                if user.detect(0,0,False) == True:
                    #print("your turn1")
                    time.sleep(0.1)
                    turn_counter += 1
                    if user.click_checker[-1] in ai.xy: #'''change setup to something else that i name the AI setup grid'''
                        #print("HIT",screen5_counter)
                        pygame.draw.rect(Display,red,(user.clicked[-2],user.clicked[-1],user.box_width,user.box_height),0) #draws a red box if a ship is hit
                        pygame.display.update()
                        screen5_counter +=1
                if screen5_counter == 9:
                    #print("screen 6")
                    screen = 6
            else:
                Display.fill(black,pygame.Rect(int(display_width/4)*3-210,610,500,50))
                pygame.draw.rect(Display,coffee,(int(display_width/4)*3-215,615,500,50),2)
                text(Display,coffee,int(display_width/4)*3-210,615,150,20,"battleships/ARLRDBD.TTF",20,"Instructions:")
                text(Display,coffee,int(display_width/4)*3-210,635,150,20,"battleships/ARLRDBD.TTF",20,"Opponents turn")
                pygame.display.flip()
                time.sleep(0.8) #for processing effects
                ai.AI_main(True)
                if len(ai.hit) == 18:
                    screen = 6
                
                #print("HIT:"+str(len(ai.hit)))
                #print("your turn")
                turn_counter += 1
                
        elif screen == 6:
            Display.fill(black,pygame.Rect(int(display_width/4)*3-212,610,520,display_height-605))
            if button(Display,coffee,(int(display_width/4)*3-215),615,145,50,2) == True:
                screen = 7
            text(Display,coffee,(int(display_width/4)*3-215),615,145,50,"battleships/ARLRDBD.TTF",40,"Results")
            
        elif screen == 7:
            Display.fill(black)
            if len(ai.hit) == 18:
                text(Display,coffee,(int(display_width/2)-262),100,525,80,"battleships/warfont.otf",100,"You Lost")
            else:
                text(Display,coffee,(int(display_width/2)-262),100,525,80,"battleships/warfont.otf",100,"You Won")

            if button(Display,coffee,(display_width/2 - 170), int(display_height/2),340,70,2) == True:
                screen = 0
            text(Display,coffee,(display_width/2 - 170), int(display_height/2),340,70,"battleships/ARLRDBD.TTF",60,"Game Menu")
            
            if button(Display,coffee,int(display_width/2 - 120), (display_height/2+150),240,75,2) == True:
                #__name__ = '__launcher__'
            #text(Display,coffee,int(display_width/2 - 120), (display_height/2+150),240,75,"battleships/ARLRDBD.TTF",60,"B.A.R.S.")
                break
            
            
        pygame.display.flip()
    pygame.quit()
    quit()
#if __name__ == '__bs__':
#    Battleships()
