import pygame
from pygame.sprite import Sprite
from settings import *
from pygame import Rect
from time import sleep


class SuperMario(Sprite):
    def __init__(self, screen, firemario=None):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('images/SuperMario/6.png')
        self.rect = self.image.get_rect()
        if firemario:
            self.screen.fill((0, 0, 0), rect=firemario.rect)
            self.rect.centerx = firemario.rect.centerx
            self.rect.bottom = firemario.rect.bottom
            del firemario
        else:
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = (GROUND_HEIGHT * BG_SCALER)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.centerx = float(self.rect.centerx)

    def blitme_faceRight_standing(self):
        self.image = pygame.image.load('images/SuperMario/6.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight_walking(self):
        self.image = pygame.image.load('images/SuperMario/7.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight_midstep(self):
        self.image = pygame.image.load('images/SuperMario/8.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceRight2_walking(self):
        self.image = pygame.image.load('images/SuperMario/9.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_standing(self):
        self.image = pygame.image.load('images/SuperMario/5.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_walking(self):
        self.image = pygame.image.load('images/SuperMario/4.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_midstep(self):
        self.image = pygame.image.load('images/SuperMario/3.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft2_walking(self):
        self.image = pygame.image.load('images/SuperMario/2.png')
        self.screen.blit(self.image, self.rect)

    def blitme_faceLeft_gliding(self, stats):
        self.image = pygame.image.load('images/SuperMario/1.png')
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()
        sleep(.05)
        x = 0
        while x < 4:
            self.screen.fill((0, 0, 0), rect=self.rect)
            self.centerx -= 5
            self.rect.centerx = self.centerx
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()
            sleep(.08)
            x += 1
        stats.frame_curr = 0

    def blitme_faceRight_gliding(self, stats):
        self.image = pygame.image.load('images/SuperMario/10.png')
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
            self.image = pygame.image.load('images/SuperMario/0.png')
            self.screen.blit(self.image, self.rect)
        if stats.mario_facing_right:
            self.image = pygame.image.load('images/SuperMario/11.png')
            self.screen.blit(self.image, self.rect)

    def blitme_crouch(self, stats):
        if stats.mario_facing_left:
            self.image = pygame.image.load('images/SuperMario/12.png')
        if stats.mario_facing_right:
            self.image = pygame.image.load('images/SuperMario/13.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.centerx
        self.rect.bottom = (GROUND_HEIGHT * BG_SCALER)
        self.screen.blit(self.image, self.rect)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_walking(self, stats):
        if stats.mario_moving_left or stats.mario_moving_right:
            self.screen.fill((0, 0, 0), rect=self.rect)
        self.update_image_dims()
        if stats.mario_moving_right and self.rect.right < self.screen_rect.right:
            if stats.frame_curr > 5:
                stats.frame_curr = .05
            self.centerx += 1.2
            stats.frame_curr += .05
        if stats.mario_moving_left and self.rect.left > 0:
            if stats.frame_curr < -5:
                stats.frame_curr = -.05
            self.centerx -= 1.2
            stats.frame_curr -= .05
        if not stats.mario_moving_left and not stats.mario_moving_right:
            stats.frame_curr = 0

        self.rect.centerx = self.centerx
        self.rect.left = self.rect.left
        self.rect.bottom = (GROUND_HEIGHT * BG_SCALER)

    def jump_straight(self, stats):
        x = 0
        while x < 5:
            self.screen.fill((0, 0, 0), rect=self.rect)
            self.rect.top -= self.height/5
            self.blitme_jump(stats)
            pygame.display.flip()
            sleep(.01)
            x += 1
        x = 0
        while x < 5:
            self.screen.fill((0, 0, 0), rect=self.rect)
            self.rect.top += self.height/5
            self.blitme_jump(stats)
            pygame.display.flip()
            sleep(.01)
            x += 1
        return self

    def jump_side(self, stats):
        stats.test = True
        x = 0
        while x < 5:
            self.screen.fill((0, 0, 0), rect=self.rect)
            self.rect.top -= self.height/5
            if stats.mario_moving_right:
                self.rect.left += self.width / 5
                self.centerx += self.width / 5
            elif stats.mario_moving_left:
                self.rect.left -= self.width / 5
                self.centerx -= self.width / 5
            self.blitme_jump(stats)
            pygame.display.flip()
            sleep(.05)
            x += 1
        x = 0
        while x < 5:
            self.screen.fill((0, 0, 0), rect=self.rect)
            self.rect.top += self.height/5
            if stats.mario_moving_right:
                self.centerx += self.width / 5
                self.rect.left += self.width / 5
            elif stats.mario_moving_left:
                self.centerx -= self.width / 5
                self.rect.left -= self.width / 5
            self.blitme_jump(stats)
            pygame.display.flip()
            sleep(.05)
            x += 1
        self.rect.centerx = self.centerx
        stats.mario_walking = True
        if stats.mario_moving_right:
            self.blitme_faceRight_standing()
        elif stats.mario_moving_left:
            self.blitme_faceLeft_standing()

    def curr_frame_walking(self, stats):
        self.screen.fill((0, 0, 0), rect=self.rect)
        if stats.frame_curr > 0:
            stats.mario_facing_right = True
            stats.mario_facing_left = False
        elif stats.frame_curr < 0:
            stats.mario_facing_left = True
            stats.mario_facing_right = False

        if stats.frame_curr == 0 and not stats.mario_crouching:
            if stats.mario_facing_left:
                self.blitme_faceLeft_walking()
            elif stats.mario_facing_right:
                self.blitme_faceRight_walking()
        elif 0 < stats.frame_curr < 1:
            self.blitme_faceRight_walking()
        elif int(stats.frame_curr) == 2:
            self.blitme_faceRight_midstep()
        elif int(stats.frame_curr) == 3:
            self.blitme_faceRight2_walking()
        elif int(stats.frame_curr) == 4:
            self.blitme_faceRight_midstep()
        elif -1 < int(stats.frame_curr) < 0:
            self.blitme_faceLeft_walking()
        elif int(stats.frame_curr) == -2:
            self.blitme_faceLeft_midstep()
        elif int(stats.frame_curr) == -3:
            self.blitme_faceLeft2_walking()
        elif int(stats.frame_curr) == -4:
            self.blitme_faceLeft_midstep()

    def update_image_dims(self):
        self.width = self.image.get_width()
