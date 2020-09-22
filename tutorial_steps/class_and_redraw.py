import pygame
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

    def redraw(self):
        #Nothing to redraw for now
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
