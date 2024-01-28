import pygame

TILE_SIZE = 50

HEIGHT = 500
WIDTH = 1500

win = pygame.display.set_mode((WIDTH,HEIGHT))
windowCaption = pygame.display.set_caption("Fire Boy")

class World():
    def __init__(self,data):
        self.tileList = []

        self.goal = None

        brick = pygame.image.load('img/brick.png')
        campfire = pygame.image.load('img/campfire.png')

        rowCount = 0
        for row in data:
            columnCount = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(brick,(TILE_SIZE,TILE_SIZE))
                    imgRect = img.get_rect()
                    imgRect.x = columnCount * TILE_SIZE
                    imgRect.y = rowCount * TILE_SIZE
                    tile = (img, imgRect)
                    self.tileList.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(campfire,(TILE_SIZE,TILE_SIZE))
                    self.goal = img
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
    
    def getGoal(self):
        return self.goal 

world1Data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
    
    
