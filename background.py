import pygame
import sys
from settings import *
import os

__all__ = ['Background']


class Background:
    def __init__(self, screen, level):
        self.bg = []
        for i in range(1, 9):
            self.bg.append(pygame.image.load('images/bg/bg-{}.jpg'.format(str(i))))

        for i in range(len(self.bg)):
            self.bg[i] = pygame.transform.scale(self.bg[i],
                                                (int(self.bg[i].get_rect().width * BG_SCALER),
                                                 int(self.bg[i].get_rect().height * BG_SCALER)))
        self.coins = 0
        self.background = self.bg[0]
        self.screen = screen
        self.background_rect = self.bg[0].get_rect()
        self.level = level
        self.x = 0
        self.blocks = pygame.sprite.Group()
        self.brick_group = pygame.sprite.Group()
        self.coin_boxes = pygame.sprite.Group()

        self.coin_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()
        self.shroom_group = pygame.sprite.Group()
        self.finish_flag = None
        self.setup()
        self.top = False
        self.view_point_x = None
        self.view_point_y = None
        self.panned_right = False
        self.panned = False
        self.bg_length = None
        self.bg_height = None

    def start(self):
        if not self.panned_right:
            self.pan_screen()
        elif not self.panned:
            self.pan_left()

    def draw(self):
        if not self.panned:
            self.start()
        # self.move_screen(2)
        self.screen.blit(self.bg[self.level], (self.x, 0))
        # print(self.ground)

    def move_items(self, vel):
        for coin in self.coin_group.sprites():
            coin.rect.x -= vel
        for powerup in self.powerup_group.sprites():
            powerup.rect.x -= vel
        for shroom in self.shroom_group.sprites():
            shroom.rect.x -= vel
        for coin_box in self.coin_boxes.sprites():
            coin_box.rect.x -= vel
        for block in self.blocks.sprites():
            block.rect.x -= vel
        for brick in self.brick_group.sprites():
            brick.rect.x -= vel
        self.finish_flag.rect.x -= vel


    def move_screen(self, vel):
        if -self.x < self.bg[self.level].get_rect().width - self.screen.get_rect().width:
            self.x -= vel
            self.move_items(vel)
        else:
            self.finish_flag.win()

    def pan_screen(self):
        if -self.x < self.bg_length:
            self.x -= 10
            self.move_items(10)
        else:
            self.panned_right = True

    def pan_left(self):
        if -self.x > self.screen.get_rect().width:
            self.x -= -10
            self.move_items(-10)
        else:
            self.panned = True

    def new_level(self):
        if self.level < 7:
            self.x = 0  # set starting position on map
            self.level += 1

    def setup_invisible_rect(self):
        pass



    def blit_rect(self, frame_index):
        # self.blocks.draw(self.screen)
        # self.coin_boxes.update(frame_index)
        # self.coin_boxes.draw(self.screen)
        # self.brick_group.draw(self.screen)
        self.platform_group.update(frame_index)
        self.platform_group.draw(self.screen)
        self.finish_flag.draw()
        for shroom in self.shroom_group:
            if shroom.state != REVEALING:
                self.adjust_mushroom_position(shroom)



        # self.brick_group.draw()

    def setup_boxes(self):
        pass

    def setup_bricks(self):
        pass

    def setup_flag(self):
        pass

    def setup(self):
        self.setup_boxes()
        self.setup_invisible_rect()
        self.setup_bricks()
        self.setup_flag()
        self.setup_groups()

    def setup_groups(self):
        self.platform_group = pygame.sprite.Group(self.coin_boxes, self.blocks, self.brick_group)

    def check_y_collisions(self, obj):
        collider = pygame.sprite.spritecollideany(obj, self.platform_group)

        if collider:
            self.adjust_y_position(obj, collider)
        else:
            self.check_if_falling(obj, self.platform_group)

    def check_x_collisions(self, obj):
        collider = pygame.sprite.spritecollideany(obj, self.platform_group)

        if collider:

            self.adjust_x_position(obj, collider)

    def adjust_mushroom_position(self, mushroom):
        if mushroom.state != REVEALING:
            mushroom.rect.y += mushroom.y_vel
            self.check_y_collisions(mushroom)

            mushroom.rect.x += mushroom.x_vel
            self.check_x_collisions(mushroom)
            self.delete_off_screen(mushroom)

    def check_if_falling(self, obj, group):
        obj.rect.y += 1

        if pygame.sprite.spritecollideany(obj, group) is None:
            obj.state = FALLING
        else:
            obj.state = SLIDING

        obj.rect.y -= 1

    def adjust_y_position(self, obj, collider):
        # FALLING
        if obj.rect.bottom + 3 <= collider.rect.bottom:
            obj.state = SLIDING
            if obj.rect.bottom != collider.rect.top:
                obj.rect.bottom = collider.rect.top
                obj.y_vel = 0

    def adjust_x_position(self, obj, collider):
        if obj.rect.x < collider.rect.x:
            obj.rect.right = collider.rect.x
            obj.direction = LEFT
        else:
            obj.rect.x = collider.rect.right
            obj.direction = RIGHT

    def delete_off_screen(self, sprite):
        if sprite.rect.y > self.bg_height:
            sprite.kill()
        elif sprite.rect.x < 0:
            sprite.kill()





    def powerup_collisions(self, mario):
        mario_powerup = pygame.sprite.spritecollideany(mario, self.powerup_group)
        mario_shroom = pygame.sprite.spritecollideany(mario, self.shroom_group)

    def win(self):
        pass

    def mario_y_collisions(self, mario):
        coin_boxes = pygame.sprite.spritecollideany(mario, self.coin_boxes)
        bricks = pygame.sprite.spritecollideany(mario, self.brick_group)
        collider = pygame.sprite.spritecollideany(mario, self.blocks)

        if coin_boxes:
            if mario.rect.top >= coin_boxes.bottom:
                coin_boxes.state = REVEALING
                if coin_boxes.prize == COIN:
                    self.coins += 1
                mario.rect.top = coin_boxes.rect.bottom
            elif mario.rect.bottom < coin_boxes.top:
                mario.rect.bottom = coin_boxes.top

        if bricks:
            if mario.rect.top >= bricks.bottom:
                bricks.kill()
                mario.rect.top = bricks.rect.bottom
            elif mario.rect.bottom < bricks.top:
                mario.rect.bottom = bricks.top

        if collider:
            if mario.rect.bottom < collider.rect.top:
                mario.rect.bottom = collider.rect.top





if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    clock = pygame.time.Clock()
    bg = Background(screen=screen, level=0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bg.draw()
        pygame.display.flip()
        clock.tick(150)
