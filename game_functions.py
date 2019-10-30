import sys
import pygame
from time import sleep
from fireball import Fireball


def check_events(stats, mario):
    '''Respond to keyboard and mouse events.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, stats, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, stats, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()


def check_keydown_events(event, stats, mario):
    '''Respond to keypresses.'''
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and pressed[pygame.K_LEFT]:
        stats.mario_gliding = True
    if pressed[pygame.K_RIGHT]:
        pygame.key.set_repeat(10, 5000)
        stats.mario_moving_right = True
        stats.mario_walking = True
        if pressed[pygame.K_LSHIFT]:
            stats.mario_running = True
    if pressed[pygame.K_LEFT]:
        pygame.key.set_repeat(10, 5000)
        stats.mario_moving_left = True
        stats.mario_walking = True
        if pressed[pygame.K_LSHIFT]:
            stats.mario_running = True
    if pressed[pygame.K_DOWN]:
        pygame.key.set_repeat(10, 5000)
        stats.mario_crouching = True
    if pressed[pygame.K_LSHIFT]:
        if not stats.fire_mode:
            stats.mario_running = True
        else:
            stats.throwing_fire = True
            stats.fireball_collided = False
            mario.screen.fill((0, 0, 0), rect=mario.rect)
            mario.blitme_throwfire(stats)
    if pressed[pygame.K_SPACE]:
        pygame.key.set_repeat(10, 5000)
        stats.mario_jumping = True
        stats.mario_walking = False
    if pressed[pygame.K_q]:
        sys.exit()
    if pressed[pygame.K_f]:
        if stats.fire_mode:
            stats.fire_mode = False
        else:
            stats.fire_mode = True


def check_keyup_events(event, stats, mario):
    '''Respond to key releases.'''
    pressed = pygame.key.get_pressed()
    if not pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT]:
        # glide to a stop
        x = 0
        if stats.mario_moving_right or stats.mario_moving_left:
            while x < 7:
                if stats.mario_moving_right:
                    mario.centerx += 5
                    stats.frame_curr += .08
                elif stats.mario_moving_left:
                    mario.centerx -= 5
                    stats.frame_curr -= .08
                mario.update_walking(stats)
                update_screen(stats, mario)
                pygame.display.flip()
                sleep(.05)
                x += 1
        # state reflects at a stop
        stats.mario_moving_right = False
        stats.mario_moving_left = False
        stats.mario_walking = False
    elif not pressed[pygame.K_RIGHT]:
        stats.mario_moving_right = False
        if not pressed[pygame.K_LSHIFT]:
            stats.mario_running = False
    elif not pressed[pygame.K_LEFT]:
        stats.mario_moving_left = False
        if not pressed[pygame.K_LSHIFT]:
            stats.mario_running = False
    if not pressed[pygame.K_LSHIFT]:
        stats.mario_running = False
        if stats.fire_mode:
            stats.throwing_fire = False
            mario.screen.fill((0, 0, 0), rect=mario.rect)
    if not pressed[pygame.K_SPACE]:
        stats.mario_jumping = False
    if not pressed[pygame.K_DOWN] and not pressed[pygame.K_LSHIFT]:
        stats.mario_crouching = False
        if stats.mario_facing_right:
            mario.blitme_faceRight_standing()
        elif stats.mario_facing_left:
            mario.blitme_faceLeft_standing()


def update_screen(stats, mario):
    if stats.mario_walking:
        mario.curr_frame_walking(stats)
    elif stats.mario_crouching:
        mario.blitme_crouch(stats)
    elif stats.mario_jumping:
        if stats.mario_moving_right or stats.mario_moving_left:
            mario.jump_side(stats)
        else:
            mario.jump_straight(stats)

    if stats.mario_gliding:
        if stats.mario_facing_right:
            mario.blitme_faceRight_gliding(stats)
            stats.mario_facing_right = False
            stats.mario_facing_left = True
        elif stats.mario_facing_left:
            mario.blitme_faceLeft_gliding(stats)
            stats.mario_facing_right = True
            stats.mario_facing_left = False
        stats.mario_gliding = False

    if stats.frame_curr == 0:
        if not stats.mario_jumping and not stats.mario_gliding \
                and not stats.mario_crouching and not stats.throwing_fire:
            if stats.game_active:
                if stats.mario_facing_right:
                    mario.blitme_faceRight_standing()
                    mario.centerx = mario.rect.centerx
                if stats.mario_facing_left:
                    mario.blitme_faceLeft_standing()
                    mario.centerx = mario.rect.centerx
            else:
                stats.mario_facing_right = True
                mario.blitme_faceRight_standing()


