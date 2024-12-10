import pygame, random
import App

class Rock:
    def __init__( self, pos ):
        self.pos = pos
        self.asset = App.Asset( 'Sprites.Rocks' )
        self.sprites = self.asset.cut( [
            [ 0, 0, 8, 8 ],
            [ 0, 8, 8, 8 ],
            [ 8, 0, 8, 8 ],
            [ 8, 8, 8, 8 ]
        ] )
        self.sprite = self.sprites[ random.randint( 0, 3 ) ]
        self.message = 'Podnieś kamień'
    
    def render( self ):
        surf = pygame.display.get_surface()
        surf.blit( self.sprite, self.pos + App.worldOffset - pygame.Vector2( self.sprite.get_width() / 2, self.sprite.get_height() / 2 ) )