import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf_image = pygame.image.load("assets\cloud.png")
        self.surf_image = pygame.transform.scale(self.surf_image, (30, 20))
        self.surf = self.surf_image.convert()
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH +
                    100), random.randint(0, SCREEN_HEIGHT))
        )
        self.speed = 5

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.kill()
