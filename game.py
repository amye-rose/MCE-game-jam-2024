import pygame
pygame.init()

# Creates the window the game will be played in
win = pygame.display.set_mode((500,500))

# This loads the image that's used for the character sprite
char = pygame.image.load('img/fire.png')

# Class that hold all the variables for player's coordinates and character other character information
class Player(object):
    def __init__(self,x,y,width,height):
        # I'm leaving out information regarding whether the character is facing left or right, because I'm not sure
        # If we're doing walk cycle animations or not
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10

    def draw(win):
        win.blit(char,(player.x,player.y))

def redrawGameWindow():
    win.fill((0,0,0))
    win.blit(char,(player.x,player.y))
    pygame.display.update()

# This calls the "Player" class and basically just creates an instance of our character 
# So we can use the variables stored in the class
player = Player(300,410,64,64)
run = True
# While "run" is True, this loop will be active and the game will run
while run:
    pygame.time.delay(50)
    # Checks if the game has been quit out of, and if it has, sets "run" to False and ends the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # These control horizontal movement
    if keys[pygame.K_LEFT]:
        player.x -= player.velocity
    if keys[pygame.K_RIGHT]:
        player.x += player.velocity

    # Checks is "isJump" is False, and if the spacebar is pressed, sets that value to True
    if not (player.isJump):
        if keys[pygame.K_SPACE]:
            player.isJump = True
    else:
        # I'll explain how this works later, but basically this is what happens when "isJump" is True
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redrawGameWindow()

pygame.quit()