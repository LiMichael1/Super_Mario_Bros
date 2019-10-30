import pygame
from spritesheet import SpriteSheet
import sys

class Mario(pygame.sprite.Sprite):
    sheet = SpriteSheet('images/mario.png')
    standing = []
    swimming = []
    cell_width = int(405/14)
    cell_height = int(188/6)
    death = sheet.image_at((0, 12, cell_width-3, cell_height-3))
    death_rect = death.get_rect()
    death_rect.centerx = 600
    death_rect.centery = 400

    def __init__(self, screen):
        super().__init__()

        # ESTABLISH SELF IMAGE FOR PARENT CLASS
        #self.image = None

        # INITIALIZE RECT, SO YOU CAN MOVE IT
        #self.rect = self.image.get_rect()

        # DETERMINE MOVEMENTS OF MARIO
        self.swimming = False
        self.walking = True
        self.running = False
        self.status = 'normal'
        self.left = False
        self.right = True
        self.screen = screen

    def draw(self):
        pass

    def move(self):
        if self.right and self.standing:
            pass
        # check for boundaries
        pass

    def hit(self):
        pass

    def dead(self):
        self.screen.blit(Mario.death, Mario.death_rect)


if __name__ == '__main__':
    screen = pygame.display.set_mode((1200, 800))
    screen.fill((230, 32, 13))
    mario = Mario(screen)
    clock = pygame.time.Clock()
    while True:
        screen.fill((230, 32, 13))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        mario.dead()
        pygame.display.flip()
        clock.tick(50)