import pygame
import App

class Animation:
    def __init__( self, asset, map, seq, cooldown = 100 ):
        self.asset = App.Asset( asset )
        self.sprites = self.asset.cut( map )
        self.seq = seq

        self.currentSeqName = None
        self.currentSeq = None
        self.currentFrame = 0

        self.cooldown = App.Cooldown( cooldown )
        self.cooldown.start()

    def update( self ):
        self.cooldown.update()

        if not self.cooldown.running:
            self.cooldown.start()
            self.currentFrame += 1
            if self.currentFrame >= len( self.currentSeq ) - 1:
                if self.currentSeq[ len( self.currentSeq ) - 1 ] == 1:
                    self.currentFrame = 0
                else:
                    self.currentFrame = len( self.currentSeq ) - 2
    
    def render( self, pos, facing ):
        surf = pygame.display.get_surface()
        surf.blit( pygame.transform.flip( self.sprites[ self.currentSeq[ self.currentFrame ] ], facing, 0 ), pos )

    def setSeq( self, name ):
        self.currentFrame = 0
        self.currentSeq = self.seq[ name ]
        self.currentSeqName = name

    def getCurrentSprite( self ):
        return self.sprites[ self.currentSeq[ self.currentFrame ] ]