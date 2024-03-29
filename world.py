import pygame
import time

TILE_SIZE = 50

HEIGHT = 500
WIDTH = 1500

bg = pygame.image.load('img/bg2.png')
bg_scaled = pygame.transform.scale(bg,(1500,500))

win = pygame.display.set_mode((WIDTH,HEIGHT))
windowCaption = pygame.display.set_caption("A Walk in the Dark")

class World():
    def __init__(self,data,worldNum=1):
        self.tileList = []
        self.worldNum = worldNum
        if self.worldNum == 2:
            self.ending = True
        else:
            self.ending = False

        self.goal = None
        self.goalColumn = 0
        self.goalRow = 0

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
                    self.goalColumn = columnCount
                    self.goalRow = rowCount
                    imgRect = img.get_rect()
                    imgRect.x = columnCount * TILE_SIZE
                    imgRect.y = rowCount * TILE_SIZE
                    tile = (img, imgRect)
                    self.tileList.append(tile)
                columnCount += 1
            rowCount += 1
        
    def draw(self):
        win.blit(bg_scaled,(0,0))
        for tile in self.tileList:
            win.blit(tile[0],tile[1])
    
    def getGoal(self):
        return self.goal
    
    def nextWorld(self):
        pygame.event.wait(99999999)
        pygame.event.wait(99999999)
        if self.worldNum == 1:
            windowCaption = pygame.display.set_caption("Level 2")
            return World(world2Data,2)
        if self.worldNum == 2:
            return World(world2Data,2)
        time.sleep(0.01)

world1Data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,2,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1],
    [1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
    
world2Data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]   
