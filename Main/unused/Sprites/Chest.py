# player.py
import pygame

class Chest(pygame.sprite.Sprite):
    def __init__(self, width, height, placeWidth, placeHeight):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.center = (placeWidth / 4, placeHeight / 4)

    def update(self):
        # Implement any additional update logic here if needed
        pass