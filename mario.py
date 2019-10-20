import pygame
from spritesheet import SpriteSheet


class Mario(pygame.sprite.Sprite):
    sheet = SpriteSheet('')
    frames = []

    def __init__(self):
        super().__init__()

        # ESTABLISH SELF IMAGE FOR PARENT CLASS
        self.image = Mario.frames[0]

        # INITIALIZE RECT, SO YOU CAN MOVE IT
        self.rect = self.image.get_rect()

        # DETERMINE MOVEMENTS OF MARIO
        self.swimming = False
        self.walking = True
        self.running = False
        self.status = 'normal'

    def draw(self):
        pass

    def move(self):
        # check for boundaries
        pass

    def hit(self):
        pass

    def death(self):
        pass


