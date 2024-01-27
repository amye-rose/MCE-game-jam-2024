import pygame
from pygame.locals import *

import time
import math

class Control:

    def __init__(self, player):
        self._player = player
        self._go = False

    def horizontalMovement(self, keys):
        if keys[pygame.K_LEFT]:
            self._player.x -= 1
        if keys[pygame.K_RIGHT]:
            self._player.x += 1

    def jump(self):
        pass

    def stopMovement(self):
        self._go = False