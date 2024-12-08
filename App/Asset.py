import pygame

class Asset:
    def __init__( self, name ):
        self.name = name.replace( '.', '/' ) + '.png'
        self.asset = pygame.image.load( 'Assets/' + self.name ).convert_alpha()
    
    def flip( self ):
        self.asset = pygame.transform.flip( self.asset, 1, 0 )

    def getCenter( self ):
        return pygame.Vector2( self.asset.get_width() / 2, self.asset.get_height() / 2 )
    
    def cut( self, map ):
        sprites = []

        for data in map:
            sprite = pygame.Surface( ( data[ 2 ], data[ 3 ] ), pygame.SRCALPHA, 32 )
            sprite.blit( self.asset, ( 0, 0 ), data )
            sprites.append( sprite )

        return sprites