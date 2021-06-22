from obj import Obj, Pipe, Coin, Bird, Text
import pygame
import random


class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.pipes_group = pygame.sprite.Group()

        self.bg = Obj("assets/sky.png", 0, 0, self.all_sprites)
        self.bg2 = Obj("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = Obj("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Obj("assets/ground.png", 0, 480, self.all_sprites)

        self.score = Text(100, "0")

        self.bird = Bird("assets/bird1.png", 50, 320, self.all_sprites)

        self.ticks = 0

    def draw(self, window):
        self.all_sprites.draw(window)
        self.score.draw(window, 150, 50)

    def update(self):
        self.move_bg()
        self.move_ground()
        self.all_sprites.update()

        if self.bird.play:
            self.spaw_pipes()
            self.bird.colision_coin(self.coin_group)
            self.bird.colision_pipes(self.pipes_group)
            self.score.text_update(str(self.bird.pts))

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
                        random.randrange(300, 450), self.all_sprites, self.pipes_group)
            pipe2 = Pipe("assets/pipe2.png", 360,
                         pipe.rect[1] - 550, self.all_sprites, self.pipes_group)
            coin = Coin("assets/0.png", 388,
                        pipe.rect[0] - 120, self.all_sprites, self.coin_group)
