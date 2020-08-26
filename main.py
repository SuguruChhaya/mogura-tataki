'''
I should make this game so that I have to hit the space bar to actually swing the hammer. 
For this, I have to learn how to tilt pygame images. 
'''

import pygame
pygame.init()

class MainGame():
    WIDTH = 500
    HEIGHT = 500
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    def __init__(self):
        self.run = True
        self.GRASS_BG = pygame.transform.scale(pygame.image.load("images/grass.png"), (MainGame.WIDTH, MainGame.HEIGHT))
        self.ALIVE_MOLE = pygame.transform.scale(pygame.image.load('images/alive_mole.png'), (100, 100))
        self.DIRT_HOLE = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (200, 150))
        self.FPS = 60
        self.clock = pygame.time.Clock()

    #!Gets called for every while loop. Mouse movements should show here.  
    def redraw(self):
        MainGame.window.blit(self.GRASS_BG, (0,0))
        MainGame.window.blit(self.ALIVE_MOLE, (30, 30))
        MainGame.window.blit(self.DIRT_HOLE, (100, 100))
        pygame.display.update()
        
    def game_display(self):
        self.clock.tick(self.FPS)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.redraw()

        

            

game = MainGame()
game.game_display()