import pygame
import App

class Particles:
    def __init__( self, pos ):
        self.particles = [ App.Particle( pygame.Vector2( pos ) ) for i in range( 10 ) ]
    
    def update( self ):
        if len( self.particles ):
            for particle in self.particles:
                particle.update()
                if particle.fade <= 0:
                    self.particles.remove( particle )
    
    def render( self ):
        if len( self.particles ):
            for particle in self.particles:
                particle.render()
