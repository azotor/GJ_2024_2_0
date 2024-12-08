import pygame
import App, Config

class MenuButton:
    def __init__( self, label ):
        self.surf = pygame.display.get_surface()
        self.centerX = self.surf.get_width() / 2

        self.label = Config.Fonts.MAINBUTTON.render( label, False, '#aaaaaa' )

        self.arrowRight = App.Asset( 'Hud.Arrow' )
        self.arrowLeft = App.Asset( 'Hud.Arrow' )
        self.arrowLeft.flip()

        self.hover = pygame.Surface( ( 300, 50 ), pygame.SRCALPHA, 32 )
        for i in range( 151 ):
            pygame.draw.rect( self.hover, ( 102, 102, 102, i ), ( i, 0, 1, 3 ) )
            pygame.draw.rect( self.hover, ( 102, 102, 102, i ), ( i, 5, 1, 40 ) )
            pygame.draw.rect( self.hover, ( 102, 102, 102, i ), ( i, 47, 1, 3 ) )
            pygame.draw.rect( self.hover, ( 102, 102, 102, i ), ( 300 - i, 0, 1, 3 ) )
            pygame.draw.rect( self.hover, ( 102, 102, 102, i ), ( 300 - i, 5, 1, 40 ) )
            pygame.draw.rect( self.hover, ( 102, 102, 102, i ), ( 300 - i, 47, 1, 3 ) )
    
    def render( self, offset, hover ):
        rect = self.label.get_rect()
        rect.center = offset
        if hover:
            self.surf.blit( self.hover, ( offset[ 0 ] - self.hover.get_width() / 2, offset[ 1 ] - self.hover.get_height() / 2 ) )
            self.surf.blit( self.arrowLeft.asset, ( rect.centerx - 50 - self.arrowLeft.asset.get_width(), offset[ 1 ] - self.arrowLeft.asset.get_height() / 2 ) )
            self.surf.blit( self.arrowRight.asset, ( rect.centerx + 50, offset[ 1 ] - self.arrowRight.asset.get_height() / 2 ) )
        self.surf.blit( self.label, rect )