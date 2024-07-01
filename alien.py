import pygame, random

class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        path = f"Graphics/alien_{type}_64px.png"
        self.base_image = pygame.image.load(path)
        if type == 8:
            self.image = pygame.transform.scale(self.base_image, (128, 132))
        elif type == 9:
            self.image = pygame.transform.scale(self.base_image, (164, 164))
        else:
            self.image = pygame.transform.scale(self.base_image, (50, 50))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.hits=0
        self.max_hits = self.set_max_hits(type)

    def set_max_hits(self, type):
        if type == 1:
            return 1
        if type == 2:
            return 2
        if type == 3:
            return 3
        if type == 4:
            return 4
        if type == 5:
            return 5
        if type == 8:
            return 20
        if type == 9:
            return 30

    def update(self, direction):
        self.rect.x +=direction

class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.base_image = pygame.image.load("Graphics/mystery_ship_64px.png")
        self.image = pygame.transform.scale(self.base_image, (50, 50))

        x = random.choice([0, self.screen_width - self.image.get_width()])
        if x == 0:
            self.speed = 3
        else:
            self.speed = -3

        self.rect = self.image.get_rect(topleft = (x, 35))

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width:
            self.kill()
        elif self.rect.left < 0:
            self.kill()