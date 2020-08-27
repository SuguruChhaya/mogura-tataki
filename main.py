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
        self.HAMMER = pygame.transform.scale(pygame.image.load('images/hammer.png'), (150, 150))
        self.FPS = 60
        self.clock = pygame.time.Clock()

    #!Gets called for every while loop. Mouse movements should show here.  
    def redraw(self):
        #*Background grass, level, hits, misses
        MainGame.window.blit(self.GRASS_BG, (0,0))
        self.lives_label = self.HEADER_FONT.render(f'Lives: {None}', 1, (255, 255, 255))
        MainGame.window.blit(self.lives_label, (10, 10))
        self.level_label = self.HEADER_FONT.render(f'Level: {None}', 1, (255, 255, 255))
        MainGame.window.blit(self.level_label, (MainGame.WIDTH - self.level_label.get_width() - 10, 10))

        #!Moles will have a specific place they will spawn so that the hole properly covers the mole
        #*Mole

        #*Hole (9 holes)
        MainGame.window.blit(self.HOLE_1, (50, 200))
        MainGame.window.blit(self.HOLE_2, (250, 200))
        MainGame.window.blit(self.HOLE_3, (450, 200))
        MainGame.window.blit(self.HOLE_4, (50, 400))
        MainGame.window.blit(self.HOLE_5, (250, 400))
        MainGame.window.blit(self.HOLE_6, (450, 400))
        MainGame.window.blit(self.HOLE_7, (50, 600))
        MainGame.window.blit(self.HOLE_8, (250, 600))
        MainGame.window.blit(self.HOLE_9, (450, 600))

        #*Hammer
        #!The hammer needs to follow the cursor movements. Have to control the image in the middle. 
        hammer_x, hammer_y = pygame.mouse.get_pos()
        if hammer_x >= MainGame.WIDTH - self.HAMMER.get_width() / 2:
            hammer_x = MainGame.WIDTH - self.HAMMER.get_width()
        elif hammer_x <= self.HAMMER.get_width() / 2:
            hammer_x = 0
        else:
            hammer_x = hammer_x - self.HAMMER.get_width() / 2
        if hammer_y > MainGame.HEIGHT - self.HAMMER.get_width() / 2:
            hammer_y = MainGame.HEIGHT - self.HAMMER.get_height()
        elif hammer_y <= self.HAMMER.get_height() / 2:
            hammer_y = 0
        else:
            hammer_y = hammer_y - self.HAMMER.get_height() /2
        MainGame.window.blit(self.HAMMER, (hammer_x, hammer_y))



        pygame.display.update()
        
    def game_display(self):
        self.clock.tick(self.FPS)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.redraw()

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