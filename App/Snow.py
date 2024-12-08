import pygame, math, random
import App

class Snow:
    def __init__( self ):

        self.surf = pygame.display.get_surface()
        
        self.newA = random.randint( 45, 135 )
        self.newSpeed = random.randint( 20, 100 )
        self.a = self.newSpeed
        self.windDir = pygame.Vector2( math.cos( self.a * math.pi / 180 ), math.sin( self.a * math.pi / 180 ) ).normalize()
        self.windSpeed = self.newSpeed
        self.windCoolDown = App.Cooldown( random.randrange( 1000, 5000  ) )
        self.windCoolDown.start()
        
        self.maxflakes = 200
        self.flakes = [ App.Flake( random.randint( -6, self.surf.get_width() ), random.randint( 0, self.surf.get_height() ) ) for i in range( self.maxflakes ) ]

    def update( self ):
        self.windCoolDown.update()
        surfW = self.surf.get_width()
        surfH = self.surf.get_height()
        
        if not self.windCoolDown.running:
            self.newA = random.randint( 45, 135 )
            self.newSpeed = random.randint( 20, 100 )
            self.windCoolDown.setTimer( random.randint( 1000, 5000 ) )
            self.windCoolDown.start()

        if self.windSpeed > self.newSpeed:
            self.windSpeed -= 1
            if self.windSpeed <= self.newSpeed:
                self.windSpeed = self.newSpeed
        elif self.windSpeed < self.newSpeed:
            self.windSpeed += 1
            if self.windSpeed >= self.newSpeed:
                self.windSpeed = self.newSpeed
        if len( self.flakes ):
            for flake in self.flakes:
                flake.update( self.windDir * self.windSpeed )
                if flake.out( self.windDir[ 0 ] ):
                    self.flakes.remove( flake )
                    
        while len( self.flakes ) < self.maxflakes:
            if self.windDir[ 0 ] >= 0:
                x = random.randint( int( -surfW / 2 ), surfW )
                y = 0
                if x < -6:
                    x = -6
                    y = random.randint( 0, surfH - 10 )
            else:
                x = random.randint( 0, surfH * 2 )
                y = 0
                if x > surfW + 6:
                    x = surfW + 6
                    y = random.randint( 0, surfH - 10 )
            self.flakes.append( App.Flake( x, y ) )

    def render( self ):
        if len( self.flakes ):
            for flake in self.flakes:
                flake.render()