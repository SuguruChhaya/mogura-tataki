import pygame
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()

class MainGame():
    WIDTH = 700 
    HEIGHT = 800 

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    def __init__(self):
        self.FPS = 60 
        self.clock = pygame.time.Clock()
        self.run = True

        #Import images
        self.GRASS_BG = pygame.transform.scale(pygame.image.load('images/grass.png'), (MainGame.WIDTH, MainGame.HEIGHT))
        self.HOLE_1 = pygame.transform.scale(pygame.image.load('images/dirt_hole.png'), (150, 150))
        self.HOLE_2 = self.HOLE_1.copy()
        self.HOLE_3 = self.HOLE_1.copy()
        self.HOLE_4 = self.HOLE_1.copy()
        self.HOLE_5 = self.HOLE_1.copy()
        self.HOLE_6 = self.HOLE_1.copy()
        self.HOLE_7 = self.HOLE_1.copy()
        self.HOLE_8 = self.HOLE_1.copy()
        self.HOLE_9 = self.HOLE_1.copy()
        self.ALIVE_MOLE = pygame.transform.scale(pygame.image.load('images/alive_mole.png'), (100, 100))
        self.BEATEN_MOLE = pygame.transform.scale(pygame.image.load('images/beaten_mole.png'), (100, 100))
        self.TROLL = pygame.transform.scale(pygame.image.load('images/trollface.png'), (100, 100))
        self.HAMMER_IMAGE = pygame.transform.scale(pygame.image.load('images/hammer.png'), (100, 150))
        self.SQUEAK_AUDIO = pygame.mixer.Sound('audio/squeak.wav')
        self.LAUGH_AUDIO = pygame.mixer.Sound('audio/laugh.wav')

        #Level
        self.level = 0

        self.lives = 5

        self.mole_count = 5

        self.moles = []

        self.lost_counter = 0 

        self.HEADER_FONT = pygame.font.SysFont("comicsans", 50)


    def draw_background(self):
        MainGame.window.blit(self.GRASS_BG, (0, 0))
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

        self.draw_background()

        self.draw_hole_1()

        self.draw_hole_2()

        #Hammer is not in swinging motion
        if not (self.hammer.going_up or self.hammer.going_down):
            self.hammer.mouse_draw()

        elif self.hammer.going_down:
            #Keep on going down
            if self.hammer.current_degree < 90:
                self.hammer.swing_down()

            else:
                #Hammer will then go up
                self.hammer.going_down = False
                self.hammer.going_up = True

        elif self.hammer.going_up:
            #Keep on going up
            if self.hammer.current_degree > 0:
                self.hammer.swing_up()
            
            #Stop
            else:
                self.hammer.going_down = False
                self.hammer.going_up = False
                self.hammer.image = self.hammer.original_image


            



        self.hammer.final_draw()

        pygame.display.update()

    def game_display(self):
        self.clock.tick(self.FPS)
        self.hammer = Hammer(self.HAMMER_IMAGE)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not (self.hammer.going_down or self.hammer.going_up):
                        self.hammer.going_down = True
            
            self.redraw()

class Hammer():
    def __init__(self, image):
        self.image = image

        self.mask = pygame.mask.from_surface(self.image)

        self.x = None 
        self.y = None 

        self.original_image = self.image

        self.going_down = False
        self.going_up = False

        self.current_degree = 0

        self.swing_vel = 6


    def final_draw(self):
        MainGame.window.blit(self.image, (int(self.x), int(self.y)))

    def mouse_draw(self):
        self.hammer_x, self.hammer_y = pygame.mouse.get_pos()

        #Check x
        #Check whether hammer is too right
        if self.hammer_x > MainGame.WIDTH - self.image.get_width() / 2:
            self.x = MainGame.WIDTH - self.image.get_width() 
        #Check whether hammer is too left
        elif self.hammer_x < self.image.get_width() / 2:
            self.x = 0

        else:
            self.x = self.hammer_x - self.image.get_width() / 2

        #Check y
        #Check whether the hammer is too up
        if self.hammer_y > MainGame.HEIGHT - self.image.get_height() / 2:
            self.y = MainGame.HEIGHT - self.image.get_height()

        #Check whether the hammer is too down
        elif self.hammer_y < self.image.get_height() / 2:
            self.y = 0

        else:
            self.y = self.hammer_y - self.image.get_height() / 2

    def swing_down(self):
        self.image =  self.original_image
        self.image = pygame.transform.rotate(self.image, self.current_degree)
        self.current_degree += self.swing_vel

        #Update self.x and self.y 
        self.x = self.hammer_x - self.image.get_width() / 2
        self.y = self.hammer_y - self.image.get_height() / 2


    def swing_up(self):
        self.image = self.original_image
        self.image = pygame.transform.rotate(self.image, self.current_degree)
        self.current_degree -= self.swing_vel

        self.x = self.hammer_x - self.image.get_width() /2
        self.y = self.hammer_y - self.image.get_height() / 2




    



        


    


game = MainGame()
game.game_display()