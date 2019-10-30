import pygame
from pygame.sprite import Sprite
from time import sleep


class Fireball(Sprite):
    def __init__(self, stats, firemario):
        self.screen = firemario.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/FireMario/fireball.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        if stats.mario_facing_left:
            self.rect.centerx = firemario.rect.left
        elif stats.mario_facing_right:
            self.rect.centerx = firemario.rect.right
        self.centerx = float(self.rect.centerx)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def bounce(self, stats, firemario):
        while self.rect.bottom < self.screen_rect.bottom:
            self.screen.fill((0, 0, 0), rect=self.rect)
            self.rect.top += self.height * 2
            if stats.mario_facing_right:
                self.rect.left += self.width * 2
                self.centerx += self.width * 2
            elif stats.mario_facing_left:
                self.rect.left -= self.width * 2
                self.centerx -= self.width * 2
            self.blitme_fireball()
            pygame.display.flip()
            sleep(.05)
        while self.rect.top > firemario.rect.top:
            self.screen.fill((0, 0, 0), rect=self.rect)
            self.rect.top -= self.height * 2
            if stats.mario_facing_right:
                self.centerx += self.width * 2
                self.rect.left += self.width * 2
            elif stats.mario_facing_left:
                self.centerx -= self.width * 2
                self.rect.left -= self.width * 2
            self.blitme_fireball()
            pygame.display.flip()
            sleep(.05)
        self.rect.centerx = self.centerx

    def blitme_fireball(self):
        self.image = pygame.image.load('images/FireMario/fireball.png')
        self.screen.blit(self.image, self.rect)

