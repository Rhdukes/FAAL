import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Platform, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Checkpoint, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((64, 64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bouncepad(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, bounceFactor):
        super(Bouncepad, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((175, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bounce = bounceFactor

class Slippery(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, slideFactor):
        super(Slippery, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((173, 216, 230))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bounce = slideFactor