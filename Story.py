import pygame

pygame.font.init()

SCREEN_WIDTH=750
SCREEN_HEIGHT=700

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Story:
    def __init__(self, screen, text_list, arrow_image):
        self.screen = screen
        self.text_list = text_list
        self.arrow_image = arrow_image
        self.current_text_index = 0
        self.arrow_rect = arrow_image.get_rect()
        self.arrow_rect.bottomright = (screen.get_width() - 45, screen.get_height() - 30)

    def draw(self):
        background_image = pygame.image.load("Graphics/space-stars-texture.webp")
        scaled_image = pygame.transform.scale(background_image, (750, 700))
        self.screen.blit(scaled_image, (0, 0))

        text, font = self.text_list[self.current_text_index]
        lines = text.split('\n')
        y = 50
        for line in lines:
            text_surface = font.render(line, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.screen.get_width() // 2, y)
            self.screen.blit(text_surface, text_rect)
            y += 40

        self.screen.blit(self.arrow_image, self.arrow_rect)

    def next_text(self):
        self.current_text_index += 1

    def is_last_text(self):
        return self.current_text_index == len(self.text_list) - 1
