import pygame
from pygame import mixer
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()

class MainGame():
    WIDTH = 700
    HEIGHT = 800

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self):
        self.run = True
        self.FPS = 60
        self.moles_beaten = 0
        self.level = 0
        self.lives = 5
        self.mole_count = 5
        self.moles = []
        self.movin_moles = []
        self.mole_above_time_max = self.FPS
        #Keep track of showing losing message
        self.lost_counter = 0

        self.GRASS_BG = pygame.transform.scale(pygame.image.load("images/grass.png"), (MainGame.WIDTH, MainGame.HEIGHT))
        self.HEADER_FONT = pygame.font.SysFont("comicsans", 50)
        self.HOLE_1 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_2 = self.HOLE_1.copy()
        self.HOLE_3 = self.HOLE_1.copy()
        self.HOLE_4 = self.HOLE_1.copy()
        self.HOLE_5 = self.HOLE_1.copy()
        self.HOLE_6 = self.HOLE_1.copy()
        self.HOLE_7 = self.HOLE_1.copy()
        self.HOLE_8 = self.HOLE_1.copy()
        self.HOLE_9 = self.HOLE_1.copy()
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

    def draw_background(self):
        MainGame.window.blit(self.GRASS_BG, (0, 0))
        self.lives_label = self.HEADER_FONT.render(f'Lives: {self.lives}', 1, (255, 255, 255))
        MainGame.window.blit(self.lives_label, (10, 10))
        self.level_label = self.HEADER_FONT.render(f'Level: {self.level}', 1, (255, 255, 255))

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

    def redraw(self):
        self.draw_background()

        self.draw_hole_1()
        self.draw_hole_2()

        if not (self.hammer.going_down or self.hammer.going_up):
            self.hammer.mouse_draw()

        self.hammer.final_draw()

        pygame.display.update()

    def game_display(self):
        self.clock.tick(self.FPS)
        self.hammer = Hammer(self.HAMMER_IMAGE)
        while self.run:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.hammer.can_swing:
                        self.hammer.going_down = True
                        self.hammer.mouse_x = pygame.mouse.get_pos()[0]
                        self.hammer.mouse_y = pygame.mouse.get_pos()[1]
            self.redraw()


class Hammer():
    def __init__(self, image):
        self.image = image
        self.original_image = image
        self.mask = pygame.mask.from_surface(self.image)

        self.x = None
        self.y = None
        self.swing_vel = 6
        self.can_swing = True
        self.going_down = False
        self.going_up = False
        self.current_degree = 0

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


    def collide(self, obj):
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y

        return self.mask.overlap(obj.mask, (int(offset_x), int(offset_y))) != None 

    def swing_down(self):
        self.image = self.original_image
        self.image.pygame.transform.rotate(self.image, self.current_degree)
        self.x = self.mouse_x - self.image.get_width() / 2
        self.y = self.mouse_y - self.image.get_width() / 2

        self.current_degree += self.swing_vel

    def swing_up(self):
        self.image = self.original_image
        self.image.pygame.transform.rotate(self.image, self.current_degree)
        self.x = self.mouse_x - self.image.get_width() / 2
        self.y = self.mouse_y - self.image.get_width() / 2

        self.current_degree -= self.swing_vel
    

game = MainGame()
game.game_display()

