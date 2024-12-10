import pygame
import App, Config

class Icon:
    def __init__( self ):
        self.asset = App.Asset( 'Sprites.A' )
        self.show = False
        self.showOnTargetarget = None
        self.message = ''
    
    def showOnTarget( self, target, message ):
        self.show = True
        self.target = target
        self.message = message
    
    def render( self ):
        surf = pygame.display.get_surface()
        sprite = self.target.animation.getCurrentSprite()
        message = Config.Fonts.TIP.render( self.message, False, '#222222' )

        tip = pygame.Surface( ( self.asset.asset.get_width() + message.get_width() + 15, self.asset.asset.get_height() + 10 ), pygame.SRCALPHA, 32 )
        tip.fill( ( 255, 255, 255, 200 ) )
        tip.blit( self.asset.asset, ( 5, 5 ) )
        tip.blit( message, ( self.asset.asset.get_width() + 10, 5 ) )

        surf.blit( tip, ( self.target.pos - pygame.Vector2( 0, sprite.get_height() + tip.get_height() * 3 / 4 ) + App.worldOffset - pygame.Vector2( tip.get_width() / 2, tip.get_height() / 2 ) ) )