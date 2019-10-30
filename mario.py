import pygame
from pygame import Rect
from settings import *
from Super_Mario import SuperMario
from time import sleep


class Mario(SuperMario):
    def __init__(self, mario):
        super(SuperMario, self).__init__()
        mario.screen.fill((0, 0, 0), rect=mario.rect)

        self.screen = mario.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/Mario/4.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = mario.rect.centerx
        self.rect.bottom = mario.rect.bottom

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.centerx = float(self.rect.centerx)

    def blitme_faceRight_standing(self):
        self.image = pygame.image.load('images/Mario/6.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight_walking(self):
        self.image = pygame.image.load('images/Mario/7.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight_midstep(self):
        self.image = pygame.image.load('images/Mario/8.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight2_walking(self):
        self.image = pygame.image.load('images/Mario/9.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_standing(self):
        self.image = pygame.image.load('images/Mario/5.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_walking(self):
        self.image = pygame.image.load('images/Mario/4.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_midstep(self):
        self.image = pygame.image.load('images/Mario/3.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft2_walking(self):
        self.image = pygame.image.load('images/Mario/2.png')
        self.update_image_dims()
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_gliding(self, stats):
        self.image = pygame.image.load('images/Mario/1.png')
        self.update_image_dims()
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
        self.image = pygame.image.load('images/Mario/10.png')
        self.update_image_dims()
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
            self.image = pygame.image.load('images/Mario/0.png')
            self.update_image_dims()
            self.screen.blit(self.image, self.rect)
        if stats.mario_facing_right:
            self.image = pygame.image.load('images/Mario/11.png')
            self.update_image_dims()
            self.screen.blit(self.image, self.rect)

    def blitme_crouch(self, stats):
        if stats.mario_facing_left:
            self.image = pygame.image.load('images/12.png')
            self.update_image_dims()
        if stats.mario_facing_right:
            self.image = pygame.image.load('images/13.png')
            self.update_image_dims()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.centerx
        self.rect.bottom = (GROUND_HEIGHT * BG_SCALER)
        self.screen.blit(self.image, self.rect)
