import pygame, random
import App, Config

class Particle:
    def __init__( self, pos ):
        self.pos = pos
        self.dir = pygame.Vector2(
            random.random() * 2 - 1,
            random.random() * 2 - 1
        )
        self.dir = self.dir.normalize()
        self.speed = random.randint( 10, 20 )
        self.fade = random.randint( 100, 200 )
        self.size = random.randint( 1, 3 )
    
    def update( self ):
        dt = Config.App.FPS / 1000
        if self.fade > 0:
            self.fade -= 10
            self.pos += self.dir * self.speed * dt

    def render( self ):
        surf = pygame.display.get_surface()
        particle = pygame.Surface( ( self.size, self.size ), pygame.SRCALPHA, 32 )
        pygame.draw.circle( particle, ( 20, 20, 20, self.fade ), ( self.size / 2, self.size / 2 ), self.size )
        surf.blit( particle, self.pos + App.worldOffset - pygame.Vector2( self.size / 2, self.size / 2 ) )