import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        base_image = pygame.image.load("Graphics/bullet.png")
        resized_image = pygame.transform.scale(base_image, (16, 16))
        self.image = resized_image
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height + 16 or self.rect.y < 0:
            # print("Killed")
            self.kill()

