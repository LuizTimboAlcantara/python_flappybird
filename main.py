import pygame
from game import Game
from menu import Menu


class Main:
    def __init__(self):
        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("Flappy Bird")

        self.loop = True
        self.fps = pygame.time.Clock()

        self.game = Game()
        self.menu = Menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def draw(self):
        # self.game.draw(self.window)
        # self.game.update()
        self.menu.draw(self.window)
        self.menu.update()

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.update()


Main().update()
