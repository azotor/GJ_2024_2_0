import pygame
import App

class Icon:
    def __init__( self ):
        self.asset = App.Asset( 'Sprites.A' )
        self.show = False
        self.showOnTargetarget = None
    
    def showOnTarget( self, target ):
        self.show = True
        self.target = target
    
    def render( self ):
        surf = pygame.display.get_surface()
        sprite = self.target.animation.getCurrentSprite()
        surf.blit( self.asset.asset, self.target.pos - pygame.Vector2( 0, sprite.get_height() + self.asset.asset.get_width() / 2 ) + App.worldOffset - pygame.Vector2( self.asset.asset.get_width() / 2, self.asset.asset.get_height() / 2 ) )