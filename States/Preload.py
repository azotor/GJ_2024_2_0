import pygame
import App, States

class Preload( States.State ):
    def __init__( self ):
        super().__init__()
        self.cooldown = App.Cooldown( 1000 )
        self.cooldown.start()
        self.font = pygame.font.SysFont( 'Arial', 18, True, True )
    
    def update( self ):
        if not self.cooldown.running:
            self.changeState( 'MAIN' )
        self.cooldown.update()
    
    def render( self ):
        surf = pygame.display.get_surface()
        surf.fill( '#333333' )
        pygame.draw.circle( surf, '#cccccc', ( surf.get_width() / 2, surf.get_height() / 2 ), 40 )
        text = self.font.render( "Preload", False, '#cccccc' )
        rect = text.get_rect()
        rect.center = ( surf.get_width() / 2, surf.get_height() / 2 + 60 )
        surf.blit( text, rect )