import pygame

from classes.AnimSprite import AnimSprite


class Player(AnimSprite):
    def __init__(self, file_name, frame_width=None, frame_height=None, anim_speed=0, speed=2, x=None, y=None):
        super().__init__(file_name, frame_width, frame_height, anim_speed, speed, x, y)
        self.spawn_pos = (x, y)
        self.reset()
        self.delay = 500
        self.last_shoot_time = 0
        self.bullets = pygame.sprite.Group()

    def reset(self):
        self.rect.topleft = self.spawn_pos