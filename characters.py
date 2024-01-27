import pygame
from pygame.locals import *

class Character:

    def __init__(self, image, x, y, scale=(20,20)):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, scale)
        self.x = x
        self.y = y
    
    def render(self, screen):
        screen.fill((0,0,0,0))
        screen.blit(self.image, (self.x, self.y))