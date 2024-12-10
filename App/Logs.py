import pygame
import App, Config

class Logs:
    def __init__( self ):
        self.logs = []

    def update( self ):
        if len( self.logs ):
            for log in self.logs:
                log[ 1 ].update()
                if not log[ 1 ].running:
                    self.logs.remove( log )

    def render( self ):
        if len( self.logs ):
            maxWidth = 0
            for log in self.logs:
                if log[ 0 ].get_width() > maxWidth:
                    maxWidth = log[ 0 ].get_width()
            
            surf = pygame.display.get_surface()

            logs = pygame.Surface( ( maxWidth + 40, len( self.logs * 20 ) + 40 ), pygame.SRCALPHA, 32 )
            logs.fill( ( 255, 255, 255, 128 ) )

            for i, log in enumerate( self.logs ):
                logs.blit( log[ 0 ], ( 20, 20 * ( i + 1 ) ) )

            surf.blit( logs, ( 0, 0 ) )

    def add( self, message ):
        cooldown = App.Cooldown( 5000 )
        cooldown.start()
        self.logs.append( [ Config.Fonts.TIP.render( message, False, '#222222' ), cooldown ] )