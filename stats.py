class Stats:
    def __init__(self):
        self.frame_curr = 0
        self.mario_walking = False
        self.mario_jumping = False
        self.mario_running = False
        self.mario_gliding = False
        self.mario_crouching = False

        self.mario_facing_left = False
        self.mario_facing_right = False
        self.mario_moving_left = False
        self.mario_moving_right = False

        self.fire_mode = False
        self.mini_mode = False
        self.throwing_fire = False
        self.fireball_collided = False
        self.game_active = False
