import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        base_image=pygame.image.load("Graphics/my_spaceship.png")
        resized_image=pygame.transform.scale(base_image, (64, 64))
        self.image=resized_image

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.rect=self.image.get_rect(midbottom = (self.screen_width/2, self.screen_height-60))

        self.speed = 6

        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 200
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.ogg")

        self.timer = 15000
        self.start_time = pygame.time.get_ticks()
        self.timer_expired = 0
        self.timer_active = False
        self.timer_enabled = True

    def user_input(self):
        key=pygame.key.get_pressed()
        if(key[pygame.K_RIGHT]):
            self.rect.x += self.speed
        if(key[pygame.K_LEFT]):
            self.rect.x -= self.speed
        if(key[pygame.K_SPACE] and self.laser_ready):
            # print("Timer_enabled = False")
            self.timer_enabled = False
            self.timer_active = False
            self.laser_ready = False
            laser=Laser(self.rect.center, 6, self.screen_height)
            self.lasers_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

            self.reset_timer()

    def constrain(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0

    def recharge(self):
        if not self.laser_ready:
            time = pygame.time.get_ticks()
            if time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def update_timer(self):
        if self.timer_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.timer:
                self.timer_expired = 1

    def reset_timer(self):
        if self.timer_enabled:
            self.start_time = pygame.time.get_ticks()
            self.timer_expired = 0
            self.timer_active = True

    def start_timer(self):
        if self.timer_enabled:
            self.reset_timer()

    def stop_timer(self):
        self.timer_active = False

    def update(self):
        self.user_input()
        self.constrain()
        self.lasers_group.update()
        self.recharge()
        self.update_timer()

    def reset(self):
        self.rect = self.image.get_rect(midbottom=(self.screen_width / 2, self.screen_height - 60))
        self.lasers_group.empty()
        self.reset_timer()

