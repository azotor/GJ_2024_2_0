import pygame, random
import App, Config, States

class Play( States.State ):
    def __init__( self ):
        super().__init__()
        self.prints = []
        self.printsCoolDown = App.Cooldown( 100 )
        self.particles = []
        self.particleCoolDown = App.Cooldown( 500 )
        self.rocks = []
        self.woods = []
        self.seeds = []
        self.action = False

    def postinit( self ):
        self.surf = pygame.display.get_surface()
        self.lumber = App.Lumber( pygame.Vector2() )
        self.pines = [
            App.Pine( pygame.Vector2( -100, -100 ) ),
            App.Pine( pygame.Vector2( -50, -100 ) ),
            App.Pine( pygame.Vector2( 0, -100 ) ),
            App.Pine( pygame.Vector2( 50, -100 ) ),
            App.Pine( pygame.Vector2( 100, -100 ) )
        ]
        self.snow = App.Snow()
        self.rocks = [ App.Rock( pygame.Vector2( -50 + 10 * i, 100 ) ) for i in range( 10 ) ]
        self.iconA = App.Icon()
        pine = App.Asset( 'Sprites.Pine' )
        woodSprite = pygame.Surface( ( 16, 16 ), pygame.SRCALPHA, 32  )
        woodSprite.blit( pine.asset, ( 0, 0 ), ( 16, 0 , 16, 16 ) )
        seedSprite = pygame.Surface( ( 16, 16 ), pygame.SRCALPHA, 32  )
        seedSprite.blit( pine.asset, ( 0, 0 ), ( 0, 0 , 16, 16 ) )
        rocks = App.Asset( 'Sprites.Rocks' )
        rockSprite = pygame.Surface( ( 8, 8 ), pygame.SRCALPHA, 32  )
        rockSprite.blit( rocks.asset, ( 0, 0 ) )
        offset = pygame.Vector2( self.surf.get_width() / 2, self.surf.get_height() - 40 )
        self.frames = {
            'wood' : App.Frame( offset - pygame.Vector2( 84, 0 ), woodSprite ),
            'rock' : App.Frame( offset - pygame.Vector2( 48, 0 ), rockSprite ),
            'seed' : App.Frame( offset - pygame.Vector2( 8, 0 ), seedSprite )
        }

    def update( self ):

        self.particleCoolDown.update()
        self.printsCoolDown.update()

        prevLumberPos = pygame.Vector2( self.lumber.pos )
        self.lumber.update()
        nextLumberPos = pygame.Vector2( self.lumber.pos )

        if self.lumber.animation.currentSeqName == 'walk':
            if not self.printsCoolDown.running:
                self.printsCoolDown.start()
                self.prints.append( App.Print( pygame.Vector2( self.lumber.pos ) ) )
            if not self.particleCoolDown.running and self.lumber.speed == 60:
                self.particleCoolDown.start()
                self.particles.append( App.Particles( self.lumber.pos ) )
        
        if len( self.particles ):
            for particles in self.particles:
                particles.update()
                if len( particles.particles ) == 0:
                    self.particles.remove( particles )

        if len( self.prints ):
            for step in self.prints:
                step.update()
                if step.fade == 0:
                    self.prints.remove( step )
                
        if len( self.pines ):
            for pine in self.pines:
                pine.update()

        self.snow.update()

        self.iconA.show = False

        for object in self.pines + self.rocks + self.woods + self.seeds:
            if self.lumber.pos.distance_to( object.pos ) < 10:
                if object.__class__.__name__ != 'Pine' or ( object.__class__.__name__ == 'Pine' and object.state == 2 ):
                    self.iconA.showOnTarget( self.lumber )
        
        for rock in self.rocks:
            if self.lumber.pos.distance_to( rock.pos ) < 10 and App.keyMap.A and not self.action:
                self.rocks.remove( rock )
                self.frames[ 'rock' ].add( 1 )
        
        for wood in self.woods:
            if self.lumber.pos.distance_to( wood.pos ) < 10 and App.keyMap.A and not self.action:
                self.woods.remove( wood )
                self.frames[ 'wood' ].add( 1 )
        
        for seed in self.seeds:
            if self.lumber.pos.distance_to( seed.pos ) < 10 and App.keyMap.A and not self.action:
                self.seeds.remove( seed )
                self.frames[ 'seed' ].add( 1 )
        
        for pine in self.pines:
            if self.lumber.pos.distance_to( pine.pos ) < 10 and App.keyMap.A and not self.action and pine.state == 2:
                self.lumber.animation.setSeq( 'cut' )
                pine.hit()
                if( pine.hp == 0 ):
                    for i in range( random.randint( 1, 4 ) ):
                        self.woods.append( App.Wood( pine.pos ) ) 
                    for i in range( random.randint( 0, 2 ) ):
                        self.seeds.append( App.Seed( pine.pos ) ) 

        for wood in self.woods:
            wood.update()

        for seed in self.seeds:
            seed.update()

        self.action = App.keyMap.A

        App.worldOffset -= nextLumberPos - prevLumberPos

    def render( self ):
        self.surf.fill( '#dddddd' )

        if len( self.prints ):
            for print in self.prints:
                print.render()
            
        if len( self.particles ):
            for particles in self.particles:
                particles.render()

        order = sorted( self.seeds + self.woods + self.pines + self.rocks + [ self.lumber ], key = lambda x : x.pos[ 1 ] )
        for object in order:
            object.render()

        self.snow.render()

        if self.iconA.show:
            self.iconA.render()

        for frame in self.frames.values():
            frame.render()
             
        if Config.App.DEBUG:   
            pygame.draw.line( pygame.display.get_surface(), 'blue', App.worldOffset + pygame.Vector2( -10, 0 ), App.worldOffset + pygame.Vector2( 10, 0 ) )
            pygame.draw.line( pygame.display.get_surface(), 'blue', App.worldOffset + pygame.Vector2( 0, -10 ), App.worldOffset + pygame.Vector2( 0, 10 ) )