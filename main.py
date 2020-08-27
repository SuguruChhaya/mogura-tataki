'''
I should make this game so that I have to hit the space bar to actually swing the hammer. 
For this, I have to learn how to tilt pygame images. 
'''

import pygame
pygame.init()
pygame.font.init()

class MainGame():
    WIDTH = 700
    HEIGHT =800
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    def __init__(self):
        self.run = True
        self.GRASS_BG = pygame.transform.scale(pygame.image.load("images/grass.png"), (MainGame.WIDTH, MainGame.HEIGHT))
        self.HEADER_FONT = pygame.font.SysFont("comicsans", 50)
        self.ALIVE_MOLE = pygame.transform.scale(pygame.image.load('images/alive_mole.png'), (100, 100))
        self.HOLE_1 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_2 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_3 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_4 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_5 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_6 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_7 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_8 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_9 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.BEATEN_MOLE = pygame.transform.scale(pygame.image.load('images/beaten_mole.png'), (0, 0))
        self.JOEVAN = pygame.transform.scale(pygame.image.load('images/joevan.png'), (0, 0))
        self.TROLL = pygame.transform.scale(pygame.image.load('images/trollface.png'), (0, 0))
        self.HAMMER_IMAGE = pygame.transform.scale(pygame.image.load('images/hammer.png'), (100, 150))
        self.HAMMER_IMAGE.set_colorkey((255, 255, 255))
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def draw_background(self):
        MainGame.window.blit(self.GRASS_BG, (0,0))
        self.lives_label = self.HEADER_FONT.render(f'Lives: {None}', 1, (255, 255, 255))
        MainGame.window.blit(self.lives_label, (10, 10))
        self.level_label = self.HEADER_FONT.render(f'Level: {None}', 1, (255, 255, 255))
        MainGame.window.blit(self.level_label, (MainGame.WIDTH - self.level_label.get_width() - 10, 10))

    def draw_hole(self):
        MainGame.window.blit(self.HOLE_1, (50, 200))
        MainGame.window.blit(self.HOLE_2, (250, 200))
        MainGame.window.blit(self.HOLE_3, (450, 200))
        MainGame.window.blit(self.HOLE_4, (50, 400))
        MainGame.window.blit(self.HOLE_5, (250, 400))
        MainGame.window.blit(self.HOLE_6, (450, 400))
        MainGame.window.blit(self.HOLE_7, (50, 600))
        MainGame.window.blit(self.HOLE_8, (250, 600))
        MainGame.window.blit(self.HOLE_9, (450, 600))



    #!Gets called for every while loop. Mouse movements should show here.  
    def redraw(self):
        #*Background grass, level, hits, misses
        self.draw_background()

        #!Moles will have a specific place they will spawn so that the hole properly covers the mole
        #*Mole

        #*Hole (9 holes)
        self.draw_hole()

        #*Hammer
        #!The hammer needs to follow the cursor movements. Have to control the image in the middle. 
        if not (self.hammer.going_down or self.hammer.going_up):
            self.hammer.mouse_draw()

        elif self.hammer.going_down:
            if self.hammer.current_degree < 90:
                self.hammer.swing_down()
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

        self.hammer.final_draw()

        #*Check for collision of pixels




        pygame.display.update()


        
    def game_display(self):
        self.clock.tick(self.FPS)
        self.hammer = Hammer(self.HAMMER_IMAGE)
        while self.run:
            print(self.hammer.current_degree)
            #!This forloop only runs when a new key is pressed.
            #*This makes it perfect for the space thing. 
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.run = False
                elif keys[pygame.K_SPACE]:
                    #*I think I will need an additional function to draw the hammer in motion.
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
        self.swing_vel = 1
        #*These two variables indicate whether the hammer is in the process of going_down or going_up
        self.going_down = False
        self.going_up = False
        #*Find the current degree I am at
        self.current_degree = 0
    
    #*I also need to consider cropping the image
    #*I can add arguments with the default value of the self.image's width and height
    def final_draw(self):
        MainGame.window.blit(self.image, (self.x, self.y))

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
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

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
        self.before_image, self.after_image = images
        self.above_time = above_time

    def draw(self):
        pass

        

            

game = MainGame()
game.game_display()