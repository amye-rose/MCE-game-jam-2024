# Controls kind of work and collison works
import time

import pygame
pygame.init()

HEIGHT = 500
WIDTH = 500

TILE_SIZE = 50

clock = pygame.time.Clock()
FPS = 60

win = pygame.display.set_mode((WIDTH,HEIGHT))

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('img/fire.png')
        self.image = pygame.transform.scale(img, (40, 40))
        self.imgRef = 'img/fire'
        self.direction = True
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

        self.vel_y += 1
        if self.vel_y > 10:
             self.vel_y = 10
        dy += self.vel_y

        for tile in world.tileList:
             if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                  dx = 0
             if tile[1].colliderect(self.rect.x,self.rect.y,self.width,self.height):
                if self.vel_y < 0:
                  dy = tile[1].bottom - self.rect.top
                  self.vel_y = 0
                elif self.vel_y >= 0:
                  dy = tile[1].top - self.rect.bottom
                  self.vel_y = 0
                self.jumped = 0

        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.bottom > HEIGHT:
             self.rect.bottom = HEIGHT
             dy = 0

        win.blit(self.image,self.rect)
    
    def setImg(self, img):
        self.imgRef = img[:-4:]
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (40, 40))

class World():
    def __init__(self,data):
        self.tileList = []

        dirt = pygame.image.load('img/dirt.png')

        rowCount = 0
        for row in data:
            columnCount = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt,(TILE_SIZE,TILE_SIZE))
                    imgRect = img.get_rect()
                    imgRect.x = columnCount * TILE_SIZE
                    imgRect.y = rowCount * TILE_SIZE
                    tile = (img, imgRect)
                    self.tileList.append(tile)
                columnCount += 1
            rowCount += 1
        
    def draw(self):
        win.fill((255,255,255))
        for tile in self.tileList:
            win.blit(tile[0],tile[1])

"""
def drawGrid():
	for line in range(0, 10):
		pygame.draw.line(win, (255, 255, 255), (0, line * TILE_SIZE), (WIDTH, line * TILE_SIZE))
		pygame.draw.line(win, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, HEIGHT))
"""

worldData = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]

world = World(worldData)
player = Player(100, HEIGHT)
playersize = ''

run = True
while run:

    clock.tick(FPS)

    # drawGrid()
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

    pygame.display.update()

pygame.quit()
