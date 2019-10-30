import pygame
from pygame import Rect
from Super_Mario import SuperMario
from time import sleep
from fireball import Fireball


class FireMario(SuperMario):
    def __init__(self, mario):
        super(SuperMario, self).__init__()
        mario.screen.fill((0, 0, 0), rect=mario.rect)

        self.screen = mario.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/FireMario/4.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = mario.rect.centerx
        self.rect.bottom = mario.rect.bottom

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.centerx = float(self.rect.centerx)

    def blitme_faceRight_standing(self):
        self.image = pygame.image.load('images/FireMario/6.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight_walking(self):
        self.image = pygame.image.load('images/FireMario/7.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight_midstep(self):
        self.image = pygame.image.load('images/FireMario/8.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight2_walking(self):
        self.image = pygame.image.load('images/FireMario/9.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_standing(self):
        self.image = pygame.image.load('images/FireMario/5.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_walking(self):
        self.image = pygame.image.load('images/FireMario/4.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_midstep(self):
        self.image = pygame.image.load('images/FireMario/3.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft2_walking(self):
        self.image = pygame.image.load('images/FireMario/2.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_gliding(self, stats):
        self.image = pygame.image.load('images/FireMario/1.png')
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()
        sleep(.05)
        self.screen.fill((0, 0, 0), rect=self.rect)
        x = 0
        while x < 4:
            self.centerx -= 5
            self.rect.centerx = self.centerx
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()
            sleep(.08)
            self.screen.fill((0, 0, 0), rect=self.rect)
            x += 1
        stats.frame_curr = 0

    def blitme_faceRight_gliding(self, stats):
        self.image = pygame.image.load('images/FireMario/10.png')
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()
        sleep(.05)
        self.screen.fill((0, 0, 0), rect=self.rect)
        x = 0
        while x < 4:
            self.centerx += 5
            self.rect.centerx = self.centerx
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()
            sleep(.08)
            self.screen.fill((0, 0, 0), rect=self.rect)
            x += 1
        stats.frame_curr = 0

    def blitme_jump(self, stats):
        if stats.mario_facing_left:
            self.image = pygame.image.load('images/FireMario/0.png')
            self.screen.blit(self.image, self.rect)
        if stats.mario_facing_right:
            self.image = pygame.image.load('images/FireMario/11.png')
            self.screen.blit(self.image, self.rect)

    def blitme_crouch(self, stats):
        if stats.mario_facing_left:
            self.image = pygame.image.load('images/12.png')
        if stats.mario_facing_right:
            self.image = pygame.image.load('images/13.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.screen.blit(self.image, self.rect)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def blitme_throwfire(self, stats):
        if stats.mario_facing_left:
            self.image = pygame.image.load('images/FireMario/14.png')
            self.screen.blit(self.image, self.rect)
        if stats.mario_facing_right:
            self.image = pygame.image.load('images/FireMario/15.png')
            self.screen.blit(self.image, self.rect)
        pygame.display.flip()
        fireball = Fireball(stats, self)
        fireball.bounce(stats, self)
        sleep(.04)
