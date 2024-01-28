# Controls kind of work and collison works
import time
from world import *

import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 30

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('img/fire.png')
        self.image = pygame.transform.scale(img, (40, 40))
        self.darkRef = 'img/dark'
        self.dark = pygame.image.load('%s.png' %self.darkRef)
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
        self.darkGo = True

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

        for tile in range(len(world.tileList)):
            if world.tileList[tile][1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                if world.tileList[tile][0] == world.getGoal():
                    campfire = pygame.image.load('img/campfireLit.png')
                    campfireimg = pygame.transform.scale(campfire,(TILE_SIZE,TILE_SIZE))
                    imgRect = campfireimg.get_rect()
                    imgRect.x = world.goalColumn * TILE_SIZE
                    imgRect.y = world.goalRow * TILE_SIZE
                    world.tileList[tile] = (campfireimg, imgRect)
                    player.darkGo = False
                    self.hitGoal = True
            if world.tileList[tile][1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                if self.vel_y < 0:
                  dy = world.tileList[tile][1].bottom - self.rect.top
                elif self.vel_y >= 0:
                  dy = world.tileList[tile][1].top - self.rect.bottom
                  on_ground = True
                  self.jumped = 0
                  self.vel_y = 0
                if world.tileList[tile][0] == world.getGoal():
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

        if self.darkGo:
            win.blit(self.image,self.rect)
            win.blit(self.dark,(self.rect.x-1480,self.rect.y-1480))
        if self.darkGo == False:
            win.blit(self.image,self.rect)

    
    def setImg(self, img):
        self.imgRef = img[:-4:]
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 40))

    def sendPlayer(self,x,y): 
        self.rect.x = x 
        self.rect.y = y 
        self.vel_y = 0 
        self.jumped = 0 

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
                if player.jumped < 1:
                    player.vel_y -= 15
                    player.jumped += 1
            if event.key == pygame.K_SPACE:
                if playersize != 'SS':
                    player.setImg('%sS.png' %player.imgRef)
                    playersize = playersize + 'S'
                    player.darkRef = '%sS' %player.darkRef
                    player.dark = pygame.image.load('%s.png' %player.darkRef)
        #on_event(event)
    
    if player.hitGoal:
        #if world.ending:
        #    run = False
        #player.hitGoal = False
        #player.darkRef = 'img/dark'
        #player.dark = pygame.image.load('%s.png' %player.darkRef)
        #world = world.nextWorld() 
        #player.sendPlayer(100, HEIGHT)
        pass


    pygame.display.update()

pygame.quit()
