import pygame, random
import App, Config

class Wood:
    def __init__( self, pos ):
        self.pos = pygame.Vector2( pos )
        self.dir = pygame.Vector2( random.randint( -1, 1 ), random.randint( -1, 1 ) )
        if self.dir[ 0 ] != 0 or self.dir[ 1 ] != 0:
            self.dir = self.dir.normalize()
        self.speed = random.randint( 10, 20 )
        asset = App.Asset( 'Sprites.Pine' )
        self.sprite = pygame.Surface( ( 16, 16 ), pygame.SRCALPHA, 32 )
        self.sprite.blit( asset.asset, ( 0, 0 ), ( 16, 0, 16, 16 ) )

    def update( self ):
        if self.speed > 0:
            dt = Config.App.FPS / 1000
            self.pos += self.dir * self.speed * dt
            self.speed -= 1

    def render( self ):
        surf = pygame.display.get_surface()
        surf.blit( self.sprite, self.pos + App.worldOffset - pygame.Vector2( self.sprite.get_width() / 2, self.sprite.get_height() ) )