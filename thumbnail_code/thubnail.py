
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
        #!I have created copies of folders so that the code will be the same
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
        self.HAMMER_IMAGE.set_colorkey((255, 255, 255))
        #!Only opens wav files
        #!Explain that I had lagging issues with 
        self.SQUEAK_AUDIO = pygame.mixer.Sound('audio/squeak.wav')
        self.LAUGH_AUDIO = pygame.mixer.Sound('audio/laugh.wav')

        
        self.level = 0
        '''
        self.level increase by 1 every time there are no moles left in self.moles. 
        This means, self.level is going to increase by 1 the first time I run it. 
        Therefore, self.level should be kept at 0. 
        '''
        self.lives = 5
        #!Always 5 moles
        self.moles = []

        self.mole_above_time_max = self.FPS * 1
        #For displaying lost message
        self.lost_counter = 0
        #Used to display message
        self.HEADER_FONT = pygame.font.SysFont("comicsans", 50)

        self.mole_dictionary = {
            'real_mole1': (self.ALIVE_MOLE, self.BEATEN_MOLE, self.SQUEAK_AUDIO),
            'real_mole2': (self.ALIVE_MOLE, self.BEATEN_MOLE, self.SQUEAK_AUDIO),
            'real_mole3': (self.ALIVE_MOLE, self.BEATEN_MOLE, self.SQUEAK_AUDIO),
            'real_mole4': (self.ALIVE_MOLE, self.BEATEN_MOLE, self.SQUEAK_AUDIO),
            'fake_mole': (self.TROLL, self.TROLL, self.LAUGH_AUDIO)
        }
        #*Since variable doesn't change, I can list in self 
        self.mole_coords = [(75, 250), (275, 250), (475, 250), (75, 450), (275, 450), (475, 450), (75, 650), (275, 650), (475, 650)]

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
        '''
        print(len(self.moles))
        if len(self.moles) == 0:
            self.level += 1
            #!vel can be put outside
            vel = 1 + self.level / 10
            for i in range(5):
                info = self.mole_dictionary[random.choice(list(self.mole_dictionary.keys()))]
                before, after, audio = info
                coords = random.choice(self.mole_coords)
                mole_x, mole_y = coords
                #!Will choose vel later
                
                self.moles.append((Mole(mole_x, mole_y, before, after, audio, vel)))

        #!To check whether any mole is moving
        is_moving = False
        '''
        for mole in self.moles:
            if mole.finish:
                self.moles.remove(mole)
                if mole.current_image == mole.before_image and mole.current_image != self.TROLL:
                    self.lives -= 1
            elif mole.going_up:
                mole.go_up()
                is_moving = True
            elif mole.going_down:
                mole.go_down()
                is_moving = True
            else:
                #!All the non-moving moles should be drawn first. 
                mole.draw()
        '''
        #!Could cause index error because self.moles is changed in the previous for loop
        #!Show the error and then fix
        #!Happens because len(moles) == 0 but didn't finish method yet
        try:
            if not is_moving:
                self.moles[0].going_up = True
        except IndexError:
            pass
        '''
        a = Mole(75, 450, self.TROLL, self.TROLL, self.LAUGH_AUDIO, 6)
        a.going_up = True
        
        self.moles = [a]
        self.draw_background()

        self.draw_hole_1()

        for mole in self.moles:
            if mole.going_up or mole.going_down:
                mole.draw()
        
        self.draw_hole_2()

        #!Comment out because this can change
        #self.hammer.mouse_draw()

        #When hammer is in normal state (follow mouse)
        if not (self.hammer.going_down or self.hammer.going_up):
            self.hammer.mouse_draw()
        
        elif self.hammer.going_down:
            if self.hammer.current_degree < 90:
                self.hammer.swing_down()
                for mole in self.moles:
                    if (mole.going_up or mole.going_down):
                        if self.hammer.collide(mole):
                            if mole.audio_played == False:
                                mole.audio.play()
                                mole.audio_played = True 
                            #!Lose life if hit troll
                            if mole.current_image == self.TROLL:
                                if mole.is_beaten == False:
                                    self.lives -= 1
                            mole.is_beaten = True
                            mole.current_image = mole.after_image

            else:
                self.hammer.going_down = False
                self.hammer.going_up = True
            
        elif self.hammer.going_up:
            if self.hammer.current_degree > 0:
                self.hammer.swing_up()
            else:
                self.hammer.going_down = False
                self.hammer.going_up = False
                #!Since nothing brings back to original
                self.hammer.image = self.hammer.original_image

        self.hammer.final_draw()

        if self.lives <= 0:
            lost_label = self.HEADER_FONT.render(f"Game Over: You reached Level {self.level}", 1, (255, 255, 255))
            MainGame.window.blit(lost_label, (int(MainGame.WIDTH / 2 - lost_label.get_width() /2 ), int(MainGame.HEIGHT / 2 - lost_label.get_height() / 2)))
            self.lost_counter += 1
            #!Check how long the message has been on the screen
            if self.lost_counter > self.FPS * 3:
                self.run = False

        pygame.display.update()

    def game_display(self):
        #Basic structure
        self.clock.tick(self.FPS)
        self.hammer = Hammer(self.HAMMER_IMAGE)
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not (self.hammer.going_down or self.hammer.going_up):
                        self.hammer.going_down = True
                        #!Show error about self.mouse_x
            
            self.redraw()

class Hammer():
    def __init__(self, image):
        self.image = image
        
        self.mask = pygame.mask.from_surface(self.image)
        self.x = None
        self.y = None

        #!Create self.original_image
        self.original_image = self.image

        #!Action booleans
        self.going_down = False
        self.going_up = False

        #*Degree of swinging
        self.current_degree = 0
        #!Swinging speed
        self.swing_vel = 6

    def final_draw(self):
        MainGame.window.blit(self.image, (int(self.x), int(self.y)))

    def mouse_draw(self):
        #First have to get x and y coords of hammer
        self.hammer_x, self.hammer_y = pygame.mouse.get_pos()
        #Check x
        #Check whether hammer is too right
        if self.hammer_x > MainGame.WIDTH - self.image.get_width() / 2:
            self.x = MainGame.WIDTH - self.image.get_width()
        #Check whether hammer is too left
        elif self.hammer_x < self.image.get_width() / 2:
            self.x = 0
        #Otherwise, just choose normal self.x 
        else:
            self.x = self.hammer_x - self.image.get_width() / 2
        #Check y
        #Check whether hammer is too up
        if self.hammer_y > MainGame.HEIGHT - self.image.get_width() / 2:
            self.y = MainGame.HEIGHT - self.image.get_height()
        #Check whether hammer is too down
        elif self.hammer_y < self.image.get_height() / 2:
            self.y = 0
        #Otherwise, just normal self.y
        else:
            self.y = self.hammer_y - self.image.get_height() /2

    def swing_down(self):
        #!Bringing back the image before re-rotating it
        self.image = self.original_image
        self.image = pygame.transform.rotate(self.image, self.current_degree)
        self.current_degree += self.swing_vel

        #!Demo the wacky version first then go to slide and explain
        #!how blitting changes and we always have to adjust
        self.x = self.hammer_x - self.image.get_width() / 2
        self.y = self.hammer_y - self.image.get_height() / 2

    def swing_up(self):
        #!Copy paste from swing down except subtract current degree
        self.image = self.original_image
        self.image = pygame.transform.rotate(self.image, self.current_degree)
        self.current_degree -= self.swing_vel

        #!Add after explanation
        self.x = self.hammer_x - self.image.get_width() / 2
        self.y = self.hammer_y - self.image.get_height() / 2

    #!Create new hammer method
    def collide(self, obj):
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y 
        return self.mask.overlap(obj.mask, (int(offset_x), int(offset_y))) != None



class Mole():
    def __init__(self, x, y, before_image, after_image, audio, vel):
        self.x = x
        self.y = y
        #*Use these variables to check whether mole has reached it's original spot. 
        self.original_y = y
        self.before_image = before_image
        self.after_image = after_image
        self.audio = audio
        self.current_image = before_image
        self.mask = pygame.mask.from_surface(self.current_image)
        self.vel = vel
        #*Check whether standby, going up, staying, or going down.
        self.standby = True
        self.going_up = False
        self.staying_up = False
        self.going_down = False
        #*Check whether the mole has completed one full cycle or not. 
        self.finish = False
        #*Check whether audio has been played after beaten
        self.audio_played = False
        self.is_beaten = False

        #!Add mole mask
        self.mask = pygame.mask.from_surface(self.before_image)

    def draw(self):
        MainGame.window.blit(self.current_image, (self.x, self.y))

    def go_up(self):
        #!Keep on moving down
        if self.y > self.original_y - 70:
            self.y -= self.vel
            print(self.y)
            print(self.vel)
        else:
            self.going_up = False
            self.going_down = True

    def go_down(self):
        #!Keep on going
        if self.y < self.original_y:
            self.y += self.vel
        else:
            self.going_down = False
            self.finish = True


    


game = MainGame()
game.game_display()