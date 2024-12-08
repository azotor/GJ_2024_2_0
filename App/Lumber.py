import pygame
import App, Config

class Lumber:
    def __init__( self, pos ):
        self.pos = pos
        self.dir = pygame.Vector2()
        self.speed = 30
        self.facing = 0
        self.animation = App.Animation(
            'Sprites.Lumber',
            [
                [ 0, 0, 32, 32 ],
                [ 32, 0, 32, 32 ],
                [ 64, 0, 32, 32 ],
                [ 0, 32, 32, 32 ],
                [ 32, 32, 32, 32 ]
            ],
            {
                'idle' : [ 0, 1, 2, 1, 1],
                'walk' : [ 3, 4, 1 ]
            }
        )

        self.animation.setSeq( 'idle' )
    
    def update( self ):

        dt = Config.App.FPS / 1000

        if App.keyMap.LEFT:
            self.dir[ 0 ] = -1
            self.facing = 1
        elif App.keyMap.RIGHT:
            self.dir[ 0 ] = 1
            self.facing = 0
        else:
            self.dir[ 0 ] = 0
        
        if App.keyMap.UP:
            self.dir[ 1 ] = -1
        elif App.keyMap.DOWN:
            self.dir[ 1 ] = 1
        else:
            self.dir[ 1 ] = 0

        self.speed = 60 if App.keyMap.B else 30

        if self.dir[ 0 ] != 0 or self.dir[ 1 ] != 0:
            self.dir = self.dir.normalize()
            if self.animation.currentSeqName != 'walk':
                self.animation.setSeq( 'walk' )
        else:
            if self.animation.currentSeqName != 'idle':
                self.animation.setSeq( 'idle' )

        self.pos += self.dir * self.speed * dt

        self.animation.update()

    def render( self ):
        sprite = self.animation.getCurrentSprite()
        self.animation.render( self.pos + App.worldOffset - pygame.Vector2( sprite.get_width() / 2, sprite.get_height() ), self.facing )
        if Config.App.DEBUG:
            pygame.draw.line( pygame.display.get_surface(), 'red', self.pos + App.worldOffset + pygame.Vector2( -10, 0 ), self.pos + App.worldOffset + pygame.Vector2( 10, 0 ) )
            pygame.draw.line( pygame.display.get_surface(), 'red', self.pos + App.worldOffset + pygame.Vector2( 0, -10 ), self.pos + App.worldOffset + pygame.Vector2( 0, 10 ) )