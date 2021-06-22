import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y


class Pipe(Obj):
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

    def update(self, *args):
        self.move()

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()


class Coin(Obj):
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.ticks = 0

    def update(self, *args):
        self.move()
        self.animate()

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()

    def animate(self):
        self.ticks = (self.ticks + 1) % 6
        self.image = pygame.image.load("assets/" + str(self.ticks) + ".png")


class Bird(Obj):
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.ticks = 0

    def update(self, *args):
        self.animate()
        self.move()

    def animate(self):
        self.ticks(self.ticks + 1) % 4
        self.image = pygame.image.load(
            "assets/bird" + str(self.ticks) + ".png")

    def move(self):
        key = pygame.key.pressed()

        if key[pygame.K_SPACE]:
            print("voar")
