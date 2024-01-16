import pygame
from pygame.locals import *
from .Platform import *

class Player(pygame.sprite.Sprite):
    def __init__(self, platforms, checkpoints):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((150, 75, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.velocity = pygame.Vector2(0, 0)
        self.max_fall_speed = 15
        self.jump_height = -15
        self.glide_slowdown = .75
        self.on_ground = False
        self.platforms = platforms
        self.checkpoints = checkpoints
        self.spawn_axis_x = 400
        self.spawn_axis_y = 300
        self.camera = pygame.Vector2(0, 0)
        self.last_checkpoint = None

    def handle_input(self, keys):
        self.velocity.x = keys[K_RIGHT] - keys[K_LEFT]

        if keys[K_SPACE] or keys[K_UP]:
            if self.on_ground:
                self.jump()
            elif self.velocity.y > 0:  # If player is ascending, slow down the ascent
                self.velocity.y = .5

    def jump(self):
        self.velocity.y = self.jump_height
        self.on_ground = False

    def update(self):
        gravity = 1
        self.velocity.y += gravity

        if self.velocity.y > self.max_fall_speed:
            self.velocity.y = self.max_fall_speed

        # Update position
        self.rect.x += self.velocity.x * 5
        self.check_collision_x()

        self.rect.y += self.velocity.y
        self.check_collision_y()

        if self.rect.y > 600:  # Adjusted the value to screen height
            self.reset_position()

    def reset_position(self):
        # Adjust player position based on the last checkpoint
        if self.last_checkpoint:
            self.rect.midbottom  = self.last_checkpoint

            # Calculate the offset to keep the checkpoint visible on the screen
            screen_offset_x = self.rect.centerx - self.last_checkpoint[0]
            screen_offset_y = self.rect.centery - self.last_checkpoint[1]

            # Adjust the camera position to maintain the offset
            # for sprite in self.platforms.sprites():
            #     sprite.rect.x += screen_offset_x
            #     sprite.rect.y += screen_offset_y

            # # Adjust the camera position for future rendering
            self.camera.x -= screen_offset_x
            self.camera.y -= screen_offset_y

        else:
            # If no checkpoint, reset to the middle of the screen
            self.rect.center = (400, 300)

        self.velocity = pygame.Vector2(0, 0)
        self.on_ground = True



    def check_collision_x(self):
        platforms_collisions = pygame.sprite.spritecollide(self, self.platforms, False)
        checkpoint_collisions = pygame.sprite.spritecollide(self, self.checkpoints, False)
        for platform in platforms_collisions:
            if self.velocity.x > 0:
                self.rect.right = platform.rect.left
            elif self.velocity.x < 0:
                self.rect.left = platform.rect.right
        for checkpoint in checkpoint_collisions:
            if self.velocity.x > 0:
                self.rect.right = checkpoint.rect.left
            elif self.velocity.x < 0:
                self.rect.left = checkpoint.rect.right

    def check_collision_y(self):
        all_sprites = pygame.sprite.Group()
        all_sprites.add(self.platforms, self.checkpoints)

        collisions = pygame.sprite.spritecollide(self, all_sprites, False)

        checkpoint_collision = None

        for collision in collisions:
            if isinstance(collision, Platform):
                if self.velocity.y > 0:
                    self.rect.bottom = collision.rect.top
                    self.on_ground = True
                    self.velocity.y = 0
                elif self.velocity.y < 0:
                    self.rect.top = collision.rect.bottom
                    self.velocity.y = 0
            elif isinstance(collision, Bouncepad):
                if self.velocity.y > 0:
                    self.rect.bottom = collision.rect.top
                    self.velocity.y = -collision.bounce
                elif self.velocity.y < 0:
                    self.rect.top = collision.rect.bottom
                    self.velocity.y = 0 
            elif isinstance(collision, Checkpoint):  # Adjust the class name accordingly
                checkpoint_collision = collision
                if self.velocity.y > 0:
                    self.rect.bottom = collision.rect.top
                    self.on_ground = True
                    self.velocity.y = 0
                elif self.velocity.y < 0:
                    self.rect.top = collision.rect.bottom
                    self.velocity.y = 0
            elif isinstance(collision, Slippery):
                if self.velocity.y > 0:
                    self.rect.bottom = collision.rect.top
                    self.on_ground = True
                    self.velocity.y = 0
                elif self.velocity.y < 0:
                    self.rect.top = collision.rect.bottom
                    self.velocity.y = 0

        if checkpoint_collision is not None:
            self.last_checkpoint = checkpoint_collision.rect.center

