import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 1000

VELOCITY = 5

win = pygame.display.set_mode((WIDTH,HEIGHT))

block = pygame.image.load('img/tile.png')

tileSize = 100

class Player():
    def __init__(self,x,y):

        char = pygame.image.load('img/fire.png')
        self.image = pygame.transform.scale(char, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def control(self):
        new_x = 0
        new_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            new_x -= VELOCITY
        if keys[pygame.K_RIGHT]:
            new_x += VELOCITY

        self.rect.x += new_x
        self.rect.y += new_y

    def draw(self):
        win.blit(self.image,(self.rect))

class World():
    def __init__(self,data):
        self.tileList = []

        block = pygame.image.load('img/tile.png')

        rowTotal = 0
        for row in data:
            columnTotal = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(block,(tileSize,tileSize))
                    imgRect = img.get_rect()
                    imgRect.x = columnTotal * tileSize
                    imgRect.y = rowTotal * tileSize
                    tile = (img, imgRect)
                    self.tileList.append(tile)
                columnTotal += 1
            rowTotal += 1

    def draw(self):
        for tile in self.tileList:
            win.blit(tile[0],tile[1])

worldData = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1],
]

player = Player(100,HEIGHT - 130)
world = World(worldData)

run = True
while run:

    world.draw()
    player.draw()
    player.control()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()