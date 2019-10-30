import pygame

from settings import *
from Super_Mario import SuperMario
from Fire_Mario import FireMario
from mario import Mario
import game_functions as gf
from time import sleep
from stats import Stats
from level1 import Level1

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Super Mario Bros")

    stats = Stats()

    mario = SuperMario(screen)
    mario.rect.x = screen.get_rect().centerx
    mario.rect.y = GROUND_HEIGHT * BG_SCALER
    clock = pygame.time.Clock()
    bg = Level1(screen=screen)

    frame_index = 0

    while True:
        if stats.fire_mode:
            if str(type(mario)) == "<class 'Super_Mario.SuperMario'>":
                mario = FireMario(mario)
        elif stats.mini_mode:
            if str(type(mario)) == "<class 'Super_Mario.SuperMario'>":
                mario = Mario(mario)
        else:
            if str(type(mario)) == "<class 'fire_mario.FireMario'>" \
                    or str(type(mario)) == "<class 'mario.Mario'>":
                mario = SuperMario(screen, mario)
        # mario.screen.fill((0, 0, 0), rect=mario.rect)
        gf.check_events(stats, mario)
        mario.update_walking(stats)
        frame_index += 1
        bg.draw(mario=mario)
        bg.blit_rect(frame_index=frame_index)
        gf.update_screen(stats, mario)

        pygame.display.flip()
        if not stats.mario_running:
            sleep(.002)
        if not stats.game_active:
            sleep(.5)
            stats.game_active = True
        clock.tick(FPS)

run_game()