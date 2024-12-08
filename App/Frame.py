import pygame
import App

class Frame:
    def __init__( self, pos ):
        self.pos = pos
        self.asset = App.Asset( 'Sprites.Frame' )
    
    def render( self ):
        surf = pygame.display.get_surface()
        surf.blit( self.asset.asset, self.pos - pygame.Vector2( self.asset.asset.get_width() / 2, self.asset.asset.get_height() / 2 ) ) 