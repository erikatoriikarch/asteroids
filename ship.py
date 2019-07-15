import pygame, random

class Ship(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__
        self.image = pygame.image.load('rocket.png')