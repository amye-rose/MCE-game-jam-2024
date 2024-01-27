import pygame
from pygame.locals import *

from characters import *
from controls import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 480
        self._player = Character("Images/Depression.jpg",320,240,(100,100))
        self._controller = Control(self._player)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_caption = pygame.display.set_caption("[GAME NAME HERE]")
        self._running = True
    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                self._running = False
                return
            if event.key == K_SPACE:
                self._controller.jump()
                
    def on_loop(self):
        keys = pygame.key.get_pressed()
        self._controller.horizontalMovement(keys)

    def on_render(self):
        self._player.render(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

game1 = App()
game1.on_execute()
