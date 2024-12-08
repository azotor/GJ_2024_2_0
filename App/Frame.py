import pygame
import App, Config

class Frame:
    def __init__( self, pos, icon ):
        self.pos = pos
        self.asset = App.Asset( 'Sprites.Frame' )
        self.asset.asset.blit( icon, pygame.Vector2( ( self.asset.asset.get_width() - icon.get_width() ) / 2, ( self.asset.asset.get_height() - icon.get_height() ) / 2 ) )
        self.stack = 0
    
    def render( self ):
        surf = pygame.display.get_surface()
        surf.blit( self.asset.asset, self.pos - pygame.Vector2( self.asset.asset.get_width() / 2, self.asset.asset.get_height() / 2 ) )
        counter = Config.Fonts.FRAME.render( str( self.stack ), False, 'white', 'red' )
        surf.blit( counter, self.pos - pygame.Vector2( self.asset.asset.get_width() / 2, self.asset.asset.get_height() / 2 ) + self.asset.asset.get_size() - counter.get_size() - pygame.Vector2( 2, 2 ) )
    
    def add( self, count ):
        self.stack += count