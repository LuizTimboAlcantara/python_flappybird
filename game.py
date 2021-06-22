from obj import Obj, Pipe, Coin
import pygame
import random


class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 0, 480, self.all_sprites)

        self.ticks = 0

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.move_bg()
        self.move_ground()
        self.spaw_pipes()
        self.all_sprites.update()

    def move_bg(self):
        self.bg.rect[0] -= 3
        self.bg2.rect[0] -= 3

        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 0

        if self.bg2.rect[0] <= 0:
            self.bg2.rect[0] = 360

    def move_ground(self):
        self.ground.rect[0] -= 3
        self.ground2.rect[0] -= 3

        if self.ground.rect[0] <= -355:
            self.ground.rect[0] = 0

        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 355

    def spaw_pipes(self):
        self.ticks += 1

        if self.ticks >= random.randrange(80, 110):
            self.ticks = 0
            pipe = Pipe("assets/pipe1.png", 360,
                        random.randrange(300, 450), self.all_sprites)
            pipe2 = Pipe("assets/pipe2.png", 360,
                         pipe.rect[1] - 550, self.all_sprites)
            coin = Coin("assets/0.png", 388,
                        pipe.rect[0] - 120, self.all_sprites)
