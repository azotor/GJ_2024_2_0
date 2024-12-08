import pygame

class Events:
    def __init__( self ):
        self.run = True
        pass

    def update( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

events = Events()