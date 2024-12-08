import pygame, sys
import App, Config

class Game:
    def __init__( self ):
        self.surf = pygame.display.set_mode( ( Config.App.WIDTH, Config.App.HEIGHT ), pygame.SRCALPHA, 32 )
        pygame.display.set_caption( Config.App.TITLE )

        self.clock = pygame.time.Clock()

        App.statesManager.postinit()

        App.worldOffset = pygame.Vector2( self.surf.get_width() / 2, self.surf.get_height() / 2 )

        self.loop()
        pygame.quit()
        sys.exit()
    
    def loop( self ):
        while App.events.run:
            self.update()
            self.render()

    def update( self ):
        self.clock.tick( Config.App.FPS )
        App.events.update()
        App.keys.update()
        App.statesManager.update()
    
    def render( self ):
        App.statesManager.render()

        pygame.display.update()