# Controls kind of work and collison works
import time
from world import *

import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('img/fire.png')
        self.image = pygame.transform.scale(img, (40, 40))
        self.imgRef = 'img/fire'
        self.direction = True
        self.hitGoal = False
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.direction:
                self.setImg('%sL%s.png' %(self.imgRef[:8:],self.imgRef[8:]))
                self.direction = False
            dx -= 5
        if key[pygame.K_RIGHT]:
            if self.direction == False:
                self.setImg('%s%s.png' %(self.imgRef[:8:],self.imgRef[9:]))
                self.direction = True
            dx += 5

        self.vel_y += 0.8
        if self.vel_y > 10:
             self.vel_y = 10
        dy += self.vel_y

        on_ground = False

        for tile in world.tileList:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                if tile[0] == world.getGoal():
                    self.hitGoal = True
            if tile[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                if self.vel_y < 0:
                  dy = tile[1].bottom - self.rect.top
                elif self.vel_y >= 0:
                  dy = tile[1].top - self.rect.bottom
                  on_ground = True
                  self.jumped = 0
                  self.vel_y = 0
                if tile[0] == world.getGoal():
                    self.hitGoal = True

        self.rect.x += dx
        self.rect.y += dy

        if on_ground:
            for tile in world.tileList:
                if tile[1].colliderect(self.rect.x, self.rect.y + 1, self.width, self.height):
                    self.rect.y = tile[1].top - self.height
                    break
        
        if self.rect.bottom > HEIGHT:
             self.rect.bottom = HEIGHT
             dy = 0

        dark = pygame.image.load('img/dark1.png')
        win.blit(self.image,self.rect)
        win.blit(dark,(self.rect.x-1480,self.rect.y-1480))
    
    def setImg(self, img):
        self.imgRef = img[:-4:]
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 40))

"""
def drawGrid():
	for line in range(0, 10):
		pygame.draw.line(win, (255, 255, 255), (0, line * TILE_SIZE), (WIDTH, line * TILE_SIZE))
		pygame.draw.line(win, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))
"""

world = World(world1Data)
player = Player(100, HEIGHT)
playersize = ''

bg = pygame.image.load('img/bg2.png')
bg_scaled = pygame.transform.scale(bg,(1500,500))

run = True
while run:

    clock.tick(FPS)

    win.blit(bg_scaled,(0,0))
    world.draw()
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player.jumped < 2:
                    player.vel_y -= 15
                    player.jumped += 1
            if event.key == pygame.K_SPACE:
                if playersize != 'SS':
                    player.setImg('%sS.png' %player.imgRef)
                    playersize = playersize + 'S'
        #on_event(event)
    
    if player.hitGoal:
        run = False

    pygame.display.update()

pygame.quit()
