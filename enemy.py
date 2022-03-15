import pygame
import random
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf_image = pygame.image.load(
            os.path.join('assets', 'missile.png'))
        self.surf_image = pygame.transform.scale(self.surf_image, (20, 10))
        self.surf = self.surf_image.convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH +
                    100), random.randint(0, SCREEN_HEIGHT))
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
