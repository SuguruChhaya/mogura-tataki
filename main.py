'''
I should make this game so that I have to hit the space bar to actually swing the hammer. 
For this, I have to learn how to tilt pygame images. 
'''

import pygame
from pygame import mixer
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()

class MainGame():
    WIDTH = 700
    HEIGHT =800

    #!The above time has to be in seconds
    #*I will be subtracting 60 every second
    #*So original is FPS * 3.25
    
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    def __init__(self):
        self.run = True
        self.FPS = 60
        self.moles_beaten =0
        self.level = 0
        self.lives = 5
        self.mole_count = 5
        self.moles = []
        self.moving_moles = []
        self.mole_above_time_max = self.FPS * 1
        self.lost_counter = 0
        #*mole first stay above for 3.25 seconds (3250 milliseconds). Increment every fps
        #Actual time will be max_time - 250 * self.level * FPS
        #*This way self.mole_above_time_max will be 3000 for level 1 and will decrease by 250 every level. 
        #*Every level will contain 
        

        self.GRASS_BG = pygame.transform.scale(pygame.image.load("images/grass.png"), (MainGame.WIDTH, MainGame.HEIGHT))
        self.HEADER_FONT = pygame.font.SysFont("comicsans", 50)
        self.HOLE_1 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_2 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_3 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_4 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_5 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_6 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_7 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_8 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_9 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_1.set_colorkey((255, 255, 255))
        self.HOLE_2.set_colorkey((255, 255, 255))
        self.HOLE_3.set_colorkey((255, 255, 255))
        self.HOLE_4.set_colorkey((255, 255, 255))
        self.HOLE_5.set_colorkey((255, 255, 255))
        self.HOLE_6.set_colorkey((255, 255, 255))
        self.HOLE_7.set_colorkey((255, 255, 255))
        self.HOLE_8.set_colorkey((255, 255, 255))
        self.HOLE_9.set_colorkey((255, 255, 255))
        self.ALIVE_MOLE = pygame.transform.scale(pygame.image.load('images/alive_mole.png'), (100, 100))
        self.ALIVE_MOLE.set_colorkey((255, 255, 255))
        self.BEATEN_MOLE = pygame.transform.scale(pygame.image.load('images/beaten_mole.jpg'), (100, 100))
        self.BEATEN_MOLE.set_colorkey((0,0,0))
        self.JOEVAN = pygame.transform.scale(pygame.image.load('images/joevan.png'), (100, 100))
        #?Somehow pygame recognized the collision when I set colorkey for joevan
        #?colorkey not working tho
        self.JOEVAN.set_colorkey((0,0,0))
        self.TROLL = pygame.transform.scale(pygame.image.load('images/trollface.png'), (100, 100))
        self.TROLL.set_colorkey((0, 0, 255))
        self.HAMMER_IMAGE = pygame.transform.scale(pygame.image.load('images/hammer.png'), (100, 150))
        self.SQUEAK_AUDIO = pygame.mixer.music.load('audio/squeak.mp3')
        self.LAUGH_AUDIO = pygame.mixer.music.load('audio/laugh.mp3')
        self.HAMMER_IMAGE.set_colorkey((255, 255, 255))

        self.clock = pygame.time.Clock()
        
        #*mole variables

    def draw_background(self):
        MainGame.window.blit(self.GRASS_BG, (0,0))
        self.lives_label = self.HEADER_FONT.render(f'Lives: {self.lives}', 1, (255, 255, 255))
        MainGame.window.blit(self.lives_label, (10, 10))
        self.level_label = self.HEADER_FONT.render(f'Level: {self.level}', 1, (255, 255, 255))
        MainGame.window.blit(self.level_label, (MainGame.WIDTH - self.level_label.get_width() - 10, 10))

    def draw_hole_1(self):
        #*To make the animation of the mole coming out better, I want to paste the top first, mole, then bottom.
        #*This way, the mole will be hidden when it is at the bottom, but not when it is at the top. 
        MainGame.window.blit(self.HOLE_1, (50, 200), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_2, (250, 200), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_3, (450, 200), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_4, (50, 400), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_5, (250, 400), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_6, (450, 400), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_7, (50, 600), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_8, (250, 600), (0, 0, 150, 75))
        MainGame.window.blit(self.HOLE_9, (450, 600), (0, 0, 150, 75))

    def draw_hole_2(self):
        MainGame.window.blit(self.HOLE_1, (50, 275), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_2, (250, 275), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_3, (450, 275), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_4, (50, 475), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_5, (250, 475), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_6, (450, 475), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_7, (50, 675), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_8, (250, 675), (0, 75, 150, 75))
        MainGame.window.blit(self.HOLE_9, (450, 675), (0, 75, 150, 75))


    #!Gets called for every while loop. Mouse movements should show here.  
    def redraw(self):

        #*Background moles
        if len(self.moles) == 0:    
            self.level += 1
            self.mole_count += 5
            #*Third tuple is the sound to play when beaten
            image_dict = {
                
                'real_mole1': (self.ALIVE_MOLE, self.BEATEN_MOLE, 'audio/squeak.mp3'),
                'real_mole2': (self.ALIVE_MOLE, self.BEATEN_MOLE, 'audio/squeak.mp3'),
                'real_mole3': (self.ALIVE_MOLE, self.BEATEN_MOLE, 'audio/squeak.mp3'),
                'real_mole4': (self.ALIVE_MOLE, self.BEATEN_MOLE, 'audio/squeak.mp3'),
                
            }
            #image_dict = {}
            mole_coords_tuple = [(75, 250), (275, 250), (475, 250), (75, 450), (275, 450), (475, 450), (75, 650), (275, 650), (475, 650)]
            mole_coords_tuple_copy = mole_coords_tuple.copy()
            if self.level >= 2:
                image_dict['joevan'] = (self.TROLL, self.TROLL, 'audio/laugh.mp3')
            for i in range(self.mole_count):
                images = image_dict[random.choice(list(image_dict.keys()))]
                chosen = random.choice(mole_coords_tuple_copy)
                mole_x, mole_y = chosen
                above_time = self.mole_above_time_max - (0.25 * self.FPS * self.level)

                self.moles.append(Mole(mole_x, mole_y, images, above_time))
                #self.moles.append(Mole(20, 30, ))
        
        #!First check whether there are moving moles or not.
        #*Print all the standby moles on the screen
        else:
            above_time = self.mole_above_time_max - (0.25 * self.FPS * self.level)
            print(f"above time: {above_time}")
            if len(self.moving_moles) > 0:
                for mole in self.moles:
                    if mole.going_up:
                        mole.go_up()
                        #*I don't need to change mole.going_up because that is changed in the other statement
                    elif mole.staying_up:
                        mole.stay_up()
                    elif mole.going_down:
                        mole.go_down()

                    #*I have to add an option to check whether the mole has finished the cycle. 
                    elif mole.cycle:
                        self.moles.remove(mole)
                        self.moving_moles.remove(mole)
                        #*Check whether image is after_image to see if beaten
                        if mole.current_image == mole.before_image == self.ALIVE_MOLE:
                            self.lives -= 1



                    #*Drawing the non-moving moles
                    else:
                        mole.draw()
            
            #*If moles exist but none are moving. 
            #*Since the self.moles is random, I think I can just choose the first one. 
            else:
                self.moles[0].going_up = True
                self.moving_moles.append(self.moles[0])
                    
                    

        #*Background grass, level, hits, misses
        self.draw_background()

        #*Top half of the 9 holes
        self.draw_hole_1()

        for mole in self.moving_moles:
            mole.draw()

        #!Moles will have a specific place they will spawn so that the hole properly covers the mole
        #*Moving moles (1 mole at a time)

        #*Keep track if there are any moles currently moving



        #*No moles are moving, all in standby. Choose the first mole in the list to move up. 


        #*Bottom half of the 9 holes
        self.draw_hole_2()

        #*Hammer
        #!The hammer needs to follow the cursor movements. Have to control the image in the middle. 
        if not (self.hammer.going_down or self.hammer.going_up):
            self.hammer.mouse_draw()

        elif self.hammer.going_down:
            if self.hammer.current_degree < 90:
                self.hammer.can_swing = False
                self.hammer.swing_down()
                #*Making a copy so the forloop doesn't get messed up
                for moving_mole in self.moving_moles[:]:
                    #*Check for collisions
                    if Hammer.collide(self.hammer, moving_mole):
                        #!I cannot simply remove the object after collision.
                        #*I have to swap images and let the mole follow through. 
                        if moving_mole.audio_played == False:
                            pygame.mixer.music.load(moving_mole.audio)
                            pygame.mixer.music.play()
                            moving_mole.audio_played = True
                        moving_mole.current_image = moving_mole.after_image
                        self.mole_count += 1
                    else:
                        print(moving_mole.current_image)
                        print(moving_mole.after_image)

            else:
                self.hammer.going_down = False
                self.hammer.going_up = True
        elif self.hammer.going_up:
            if self.hammer.current_degree > 0:
                self.hammer.swing_up()
            else:
                self.hammer.going_down = False
                self.hammer.going_up = False
                self.hammer.image = self.hammer.original_image
                self.hammer.can_swing = True

        self.hammer.final_draw()

        #*Check for collision of pixels

        #*Game over section
        if self.lives <= 0:
            lost_font = pygame.font.SysFont('comicsans', 30)
            lost_label = lost_font.render(f"Game Over\nYou hit {self.mole_count}", 1, (255, 255, 255))
            MainGame.window.blit(lost_label, (int(MainGame.WIDTH / 2 - lost_label.get_width() /2), 350))
            self.lost_counter += 1
            if self.lost_counter > self.FPS * 3:
                self.run = False
            
                


        pygame.display.update()


        
    def game_display(self):
        self.clock.tick(self.FPS)
        self.hammer = Hammer(self.HAMMER_IMAGE)
        while self.run:
            #!This forloop only runs when a new key is pressed.
            #*This makes it perfect for the space thing. 
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #*I think I will need an additional function to draw the hammer in motion.
                    #*Check whether a swinging motion is currently taking place
                    if self.hammer.can_swing:
                        self.hammer.going_down = True
                        #!The commented code doesn't work because the self.hammer.image.get_width() and height changes and it won't be properly centered.
                        #*This prevents the hammer to follow the cursor while hammer movement. 
                        self.hammer.mouse_x = pygame.mouse.get_pos()[0] 
                        self.hammer.mouse_y = pygame.mouse.get_pos()[1] 
            self.redraw()


class Hammer():
    '''
    I think it is beneficial to make a hammer class so the redraw method isn't over-congested. 
    '''
    def __init__(self, image):
        self.image = image
        self.original_image = image
        self.mask = pygame.mask.from_surface(self.image)
        #!There are 2 reasons why I have to define self.x and self.y
        #*1. I need to check for collision using the current coordinates. 
        #*2. The mouse movements don't solely dictate the xy coordinates and how the image is going to be drawn.
        #*I have to consider hammer swings too. 
        self.x = None
        self.y = None
        #*Swinging and bringing back speed. 
        self.swing_vel = 6
        #*These two variables indicate whether the hammer is in the process of going_down or going_up
        self.can_swing = True
        self.going_down = False
        self.going_up = False
        #*Find the current degree I am at
        self.current_degree = 0
    
    #*I also need to consider cropping the image
    #*I can add arguments with the default value of the self.image's width and height
    def final_draw(self):
        MainGame.window.blit(self.image, (int(self.x), int(self.y)))

    def mouse_draw(self):
        hammer_x, hammer_y = pygame.mouse.get_pos()
        if hammer_x >= MainGame.WIDTH - self.image.get_width() / 2:
            self.x = MainGame.WIDTH - self.image.get_width()
        elif hammer_x <= self.image.get_width() / 2:
            self.x = 0
        else:
            self.x = hammer_x - self.image.get_width() / 2
        if hammer_y > MainGame.HEIGHT - self.image.get_width() / 2:
            self.y = MainGame.HEIGHT - self.image.get_height()
        elif hammer_y <= self.image.get_height() / 2:
            self.y = 0
        else:
            self.y = hammer_y - self.image.get_height() /2


    def collision(self, obj):
        return Hammer.collide(self, obj)

    @staticmethod
    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y

        return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None

    def swing_down(self):
        '''
        This method is for swinging the hammer when the space bar is pressed. 
        It has to do a couple of things.  
        1. Modify the self.x and self.y value so the hammer is drawn at the right coordinates. 
        2. Make it so that the self.x and self.y value cannot be changed by moving the mouse while the hammer hasn't gone down and came back yet. 
        (For this, I can implement a variable in the mouse_draw method to check whether the swinging process is happening right now.)
        3. Use pygame.transform.rotate to rotate the image. Have to check whether the hammer has made a 90 degree counter-clockwise turn.
        '''
        self.image = self.original_image
        #*I am going to temporarily adjust the self.x and self.y value to the left bottom corner of the image.
        #?Ways to rotate the image 
        #!Colour key is legenday!!!
        #*I set a colourkey to exclude while on the outer part and it worked perfectly!!
        #!I cannot just add the degrees because the self.image starts off with rotated image then
        self.image = pygame.transform.rotate(self.image, self.current_degree)
        self.x = self.mouse_x - self.image.get_width() / 2
        self.y = self.mouse_y - self.image.get_height() / 2


        #*Controls the speed on swinging down
        self.current_degree += self.swing_vel

        #self.image = pygame.transform.rotate(self.image, 10)

    def swing_up(self):
        self.image = self.original_image
        self.image = pygame.transform.rotate(self.image, self.current_degree)
        self.x = self.mouse_x - self.image.get_width() / 2
        self.y = self.mouse_y - self.image.get_height() / 2
        self.current_degree -= self.swing_vel

class Mole():
    #*A mole can be an actual mole or a joevan. The have different starting pictures and pictures when they are beaten. 
    '''
    x is a randomly generated x value corresponding to the x value of the 9 holes. int
    y correspongs to the y value. int
    images will a tuple with the image before being beaten and the image after being beaten. This will be the item in a dictionary for the MainGame class. 
    above_time is the amount of time the mole stays up before going back to the hole in milliseconds. int
    '''
    def __init__(self, x, y, images, above_time):
        self.x = x
        self.y = y
        #*Use these variables to check whether mole has reached it's original spot. 
        self.original_x = x
        self.original_y = y
        self.before_image, self.after_image, self.audio = images[0], images[1], images[2]
        self.current_image = images[0]
        self.mask = pygame.mask.from_surface(self.current_image)
        self.mole_vel = 1
        self.above_time = above_time
        #*Check whether standby, going up, staying, or going down.
        self.standby = True
        self.going_up = False
        self.staying_up = False
        self.going_down = False
        #*Check whether the mole has completed one full cycle or not. 
        self.cycle = False
        #*Check whether audio has been played after beaten
        self.audio_played = False

    def draw(self):
        MainGame.window.blit(self.current_image, (self.x, self.y))

    def go_up(self):
        #*I have to check whether I the mole has reached it's limit
        #*Remember that y becomes smaller and smaller
        if self.y > self.original_y - 70:
            self.y -= self.mole_vel
            print(self.mole_vel)
        else:
            #*Change status of stay up
            self.going_up = False
            self.staying_up = True


    def stay_up(self):
        #*This method won't change but will increment the time.
        print(f"self.above_time: {self.above_time}")
        if self.above_time > 0:
            self.above_time -= 1
        else:
            self.staying_up = False
            self.going_down = True

    def go_down(self):
        if self.y < self.original_y:
            self.y += self.mole_vel
        else:
            self.going_down = False
            self.cycle = True
    

    def beaten(self):
        pass


        

            

game = MainGame()
game.game_display()