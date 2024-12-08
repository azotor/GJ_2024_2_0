import pygame
import App, Config, States

class Main( States.State ):
    def postinit( self ):
        surf = pygame.display.get_surface()

        self.fontColor = '#aaaaaa'
        self.centerX = surf.get_width() / 2

        self.currentoption = 0
        self.options = [ 'Start', 'Quit' ]
        self.cooldown = App.Cooldown( 200 )
        self.cooldown.start()

        self.title = Config.Fonts.TITLE.render( 'TITLE', False,  self.fontColor )
        self.titleRect = self.title.get_rect()
        self.titleRect.center = pygame.Vector2( self.centerX, 100 )

        self.buttons = [ App.MenuButton( label ) for label in self.options ]

    def update( self ):
        self.cooldown.update()

        if not self.cooldown.running:
            if App.keyMap.UP:
                self.cooldown.start()
                self.currentoption -= 1
                if self.currentoption < 0:
                    self.currentoption = len( self.options ) - 1
            elif App.keyMap.DOWN:
                self.cooldown.start()
                self.currentoption += 1
                if self.currentoption >= len( self.options ):
                    self.currentoption = 0

        if App.keyMap.A:
            match self.currentoption:
                case 0:
                    self.changeState( 'PLAY' )
                case 1:
                    App.events.run = False
    
    def render( self ):
        surf = pygame.display.get_surface()
        surf.fill( '#333333' )

        surf.blit( self.title, self.titleRect )
        
        for i in range( len( self.options ) ):
            self.buttons[ i ].render( pygame.Vector2( surf.get_width() / 2, 200 + i * 50 ), True if self.currentoption == i else False )
