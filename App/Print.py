import pygame, random
import App

class Print:
    def __init__( self, pos ):
        self.pos = pos
        self.size = random.randint( 1, 2 )
        self.fade = 100
        self.cooldown = App.Cooldown( random.randint( 1000, 5000 ) )
        self.cooldown.start()

    def update( self ):
        self.cooldown.update()

        if not self.cooldown.running and self.fade > 0:
            self.fade -= 1

    def render( self ):
        print = pygame.Surface( ( self.size * 2, self.size * 2 ), pygame.SRCALPHA, 32 )
        pygame.draw.circle( print, ( 102, 102, 102, self.fade ), ( self.size, self.size ), self.size )
        pygame.display.get_surface().blit( print, self.pos + App.worldOffset - pygame.Vector2( -self.size, -self.size ) )