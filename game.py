import pygame, random
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from alien import Alien
from laser import Laser
from alien import MysteryShip

class Game:
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacles()
        self.aliens_group = pygame.sprite.Group()
        self.big_alien = None
        self.boss = None
        # self.create_aliens()
        self.aliens_direction = 1
        self.alien_lasers_group = pygame.sprite.Group()
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.lives = 3
        self.run = False
        self.level = 1
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)
        self.explosion_sound = pygame.mixer.Sound("Sounds/explosion.ogg")


        self.setup_level()

    def create_obstacles(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width - (3 * obstacle_width))/4
        obstacles = []
        for i in range(3):
            offset_x = (i+1)*gap+i*obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height-200)
            obstacles.append(obstacle)
        return obstacles

    def create_aliens(self):
        for row in range(5):
            for col in range(11):
                x = 75+col*55
                y = 75+row*55

                if row==0:
                    alien_type=3
                elif row in (1,2):
                    alien_type=2
                else:
                    alien_type=1

                alien = Alien(alien_type, x, y)
                self.aliens_group.add(alien)

    def create_aliens_2(self):
        big_alien_x = 90 + 4 * 55
        big_alien_y = 80
        self.big_alien = Alien(8, big_alien_x, big_alien_y)
        self.aliens_group.add(self.big_alien)

        for row in range(5):
            for col in range(11):
                x = 75 + col * 55
                y = 75 + row * 55

                if 0 <= row <= 2 and 4 <= col <= 6:
                    continue
                if row==0:
                    alien_type=4
                elif row in (1,2):
                    alien_type=3
                else:
                    alien_type=2

                alien = Alien(alien_type, x, y)
                self.aliens_group.add(alien)

    def create_aliens_3(self):
        boss_x = 70 + 4 * 55
        boss_y = 70
        self.boss = Alien(9, boss_x, boss_y)
        self.aliens_group.add(self.boss)

        for row in range(5):
            for col in range(11):
                x = 75 + col * 55
                y = 75 + row * 55

                if 0 <= row <= 2 and 4 <= col <= 6:
                    continue
                if row==0:
                    alien_type=5
                elif row in (1,2):
                    alien_type=4
                else:
                    alien_type=3

                alien = Alien(alien_type, x, y)
                self.aliens_group.add(alien)

    def setup_level(self):
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.spaceship_group.sprite.lasers_group.empty()

        if self.level == 1:
            self.create_aliens()
        elif self.level == 2:
            self.create_aliens_2()
        elif self.level == 10:
            self.create_aliens_3()

        self.run = True

    def move_aliens(self):
        self.aliens_group.update(self.aliens_direction)

        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width:
                self.aliens_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.aliens_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)
            self.alien_lasers_group.add(laser_sprite)

    def big_alien_laser(self):
        if self.big_alien and self.big_alien.alive():
            left = (self.big_alien.rect.left, self.big_alien.rect.centery)
            center = (self.big_alien.rect.centerx, self.big_alien.rect.centery)
            right = (self.big_alien.rect.right, self.big_alien.rect.centery)

            left_laser = Laser(left, -6, self.screen_height)
            center_laser = Laser(center, -6, self.screen_height)
            right_laser = Laser(right, -6, self.screen_height)

            choice = random.choice([left_laser, center_laser, right_laser])

            self.alien_lasers_group.add(choice)
        else:
            self.big_alien = None

    def boss_laser(self):
        if self.boss and self.boss.alive():
            left = (self.boss.rect.left, self.boss.rect.centery)
            center = (self.boss.rect.centerx, self.boss.rect.centery)
            right = (self.boss.rect.right, self.boss.rect.centery)

            left_laser = Laser(left, -6, self.screen_height)
            center_laser = Laser(center, -6, self.screen_height)
            right_laser = Laser(right, -6, self.screen_height)

            move = random.choice([left_laser, center_laser, right_laser])

            self.alien_lasers_group.add(move)
        else:
            self.boss = None

    def create_mystery_ship(self):
        self.mystery_ship_group.add(MysteryShip(self.screen_width))

    def  check_for_collisions(self):
        #Spaceship
        if self.spaceship_group.sprite.lasers_group:
            for laser_sprite in self.spaceship_group.sprite.lasers_group:
                collided_aliens = pygame.sprite.spritecollide(laser_sprite, self.aliens_group, False)
                if collided_aliens:
                        self.explosion_sound.play()
                        laser_sprite.kill()
                        for alien in collided_aliens:
                            alien.hits +=1
                            if alien.hits >= alien.max_hits:
                                if alien == self.big_alien:
                                    self.big_alien = None
                                alien.kill()
                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    if self.lives != 3:
                        self.lives += 1
                    laser_sprite.kill()

                # if self.level_complete():
                #     print("Complete")

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

        #Alien
        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                for spaceship_laser in self.spaceship_group.sprite.lasers_group:
                    if pygame.sprite.collide_rect(laser_sprite, spaceship_laser):
                        laser_sprite.kill()
                        spaceship_laser.kill()

                if laser_sprite.alive():
                    for obstacle in self.obstacles:
                        if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                            laser_sprite.kill()

                if laser_sprite.alive():
                    if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                        laser_sprite.kill()
                        self.lives -= 1
                        if self.lives == 0:
                            self.game_over()

        if self.aliens_group:
            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(alien, obstacle.blocks_group, True):
                        alien.kill()

                    # if self.level_complete():
                    #     print("Complete")

                    if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                        self.game_over()

    def game_over(self):
        self.run = False

    def reset(self):
        self.run = True
        self.level = 1
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.create_aliens()
        self.obstacles = self.create_obstacles()

    def next_level(self):
        self.level += 1
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.setup_level()
        self.obstacles = self.create_obstacles()

    def secret_level(self):
        self.level = 10
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.setup_level()
        self.obstacles = self.create_obstacles()

    def level_complete(self):
        return len(self.aliens_group) == 0

