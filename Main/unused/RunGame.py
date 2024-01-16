import pygame
from pygame.locals import *
import random

from Sprites.Player import Player
from Sprites.Platform import *

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Platformer')

clock = pygame.time.Clock()
camera = pygame.Vector2(0, 0)

# Create player and platforms
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
checkpoints = pygame.sprite.Group()
stable_sprites = pygame.sprite.Group()

player = Player(platforms, checkpoints)
all_sprites.add(player)

platform1 = Platform(100, 500, 200, 20)
platform2 = Platform(400, 400, 200, 20)
platform3 = Platform(200, 300, 200, 20)
checkpoint1 = Checkpoint(500, 300, 200, 20)
bouncepad1 = Bouncepad(0, 450, 100, 5, 25)
slippery1 = Slippery(600, 500, 600, 20, 1)


all_sprites.add(platform1, platform2, platform3, checkpoint1, bouncepad1, slippery1)
platforms.add(platform1, platform2, platform3, bouncepad1, slippery1)
checkpoints.add(checkpoint1)
stable_sprites.add(platform1, platform2, platform3, checkpoint1, bouncepad1, slippery1)


# Main game loop
all_sprites.draw(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Handle player input and update game state
    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    player.update()

    # Update camera position based on player's position or other logic
    camera.x = player.rect.x - width // 2  # Adjust as needed

    # Render game objects
    screen.fill((255, 255, 255))
    for sprite in all_sprites:
        screen.blit(sprite.image, (sprite.rect.x - camera.x, sprite.rect.y - camera.y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

