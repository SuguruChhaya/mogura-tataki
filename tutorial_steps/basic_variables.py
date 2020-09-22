import pygame
from pygame import mixer
import random
#Creates weird errors when we don't intialize
pygame.init()
pygame.font.init()
pygame.mixer.init()

class MainGame():
    WIDTH = 700
    HEIGHT = 800

    #Set up basic window
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self):
        #Screen refreshes 60 times a second. 
        self.FPS = 60
        #Used for the refreshing process
        self.clock = pygame.time.Clock()
        #Keep on refreshing or not boolean
        self.run = True


        #Importing images
        self.GRASS_BG = pygame.transform.scale(pygame.image.load('images/grass.png'), (MainGame.WIDTH, MainGame.HEIGHT))
        self.HOLE_1 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_1.set_colorkey((255, 255, 255))
        #Set colorkey and then copy
        self.HOLE_2 = self.HOLE_1.copy()
        self.HOLE_3 = self.HOLE_1.copy()
        self.HOLE_4 = self.HOLE_1.copy()
        self.HOLE_5 = self.HOLE_1.copy()
        self.HOLE_6 = self.HOLE_1.copy()
        self.HOLE_7 = self.HOLE_1.copy()
        self.HOLE_8 = self.HOLE_1.copy()
        self.HOLE_9 = self.HOLE_1.copy()
        self.ALIVE_MOLE = pygame.transform.scale(pygame.image.load('images/alive_mole.png'), (100, 100))
        self.ALIVE_MOLE.set_colorkey((255, 255, 255))
        self.BEATEN_MOLE = pygame.transform.scale(pygame.image.load('images/beaten_mole.jpg'), (100, 100))
        self.BEATEN_MOLE.set_colorkey((0,0,0))
        #!Not using Joevan this time
        self.TROLL = pygame.transform.scale(pygame.image.load('images/trollface.png'), (100, 100))
        self.TROLL.set_colorkey((0, 0, 255))
        self.HAMMER_IMAGE = pygame.transform.scale(pygame.image.load('images/hammer.png'), (100, 150))
        self.SQUEAK_AUDIO = pygame.mixer.music.load('audio/squeak.mp3')
        self.LAUGH_AUDIO = pygame.mixer.music.load('audio/laugh.mp3')
        self.HAMMER_IMAGE.set_colorkey((255, 255, 255))
        self.SQUEAK_AUDIO = pygame.mixer.music.load('audio/squeak.mp3')
        self.LAUGH_AUDIO = pygame.mixer.music.load('audio/laugh.mp3')

        #Keep track of beaten moles
        self.moles_beaten =0
        
        self.level = 0
        '''
        self.level increase by 1 every time there are no moles left in self.moles. 
        This means, self.level is going to increase by 1 the first time I run it. 
        Therefore, self.level should be kept at 0. 
        '''
        self.lives = 5
        self.mole_count = 5
        self.moles = []
        #!Don't create moving moles for now!!
        self.mole_above_time_max = self.FPS * 1
        #For displaying lost message
        self.lost_counter = 0
        #Used to display message
        self.HEADER_FONT = pygame.font.SysFont("comicsans", 50)

    #*Since the lives and level in the background always update, I have to constantly
    #*blit the background and the labels
    def draw_background(self):
        MainGame.window.blit(self.GRASS_BG, (0,0))
        self.lives_label = self.HEADER_FONT.render(f'Lives: {self.lives}', 1, (255, 255, 255))
        MainGame.window.blit(self.lives_label, (10, 10))
        self.level_label = self.HEADER_FONT.render(f'Level: {self.level}', 1, (255, 255, 255))
        MainGame.window.blit(self.level_label, (MainGame.WIDTH - self.level_label.get_width() - 10, 10))

    def draw_hole_1(self):
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

    def redraw(self):
        #Nothing to redraw for now
        self.draw_background()

        self.draw_hole_1()

        self.draw_hole_2()


        pygame.display.update()

    def game_display(self):
        #Basic structure
        self.clock.tick(self.FPS)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            
            self.redraw()

game = MainGame()
game.game_display()
