import pygame, random
import App, Config

class Pine:
    def __init__( self, pos ):
        self.pos = pos
        self.asset = App.Asset( 'Sprites/Pine' )
        self.sprite = self.asset.cut( [
            [ 16, 32, 16, 16 ],
            [ 0, 16, 16, 32 ],
            [ 32, 0, 32, 64 ],
            [ 0, 48, 32, 16 ]
        ] )
        self.state = 0
        self.growCooldown = App.Cooldown( random.randint( 5000, 10000 ) )
        self.growCooldown.start()
        self.hp = 3
        self.message = 'Zetnij sosnę'
    
    def update( self ):
            
        if self.hp <= 0:
            self.hp = 0
            self.state = 3
        
        self.growCooldown.update()

        if not self.growCooldown.running and self.state < 2:
            self.state += 1
            self.growCooldown.start()

    def render( self ):
        surf = pygame.display.get_surface()
        sprite = self.sprite[ self.state ]
        surf.blit( sprite, self.pos + App.worldOffset - pygame.Vector2( sprite.get_width() / 2, sprite.get_height() ) )
        if Config.App.DEBUG:
            pygame.draw.line( pygame.display.get_surface(), 'green', self.pos + App.worldOffset + pygame.Vector2( -10, 0 ), self.pos + App.worldOffset + pygame.Vector2( 10, 0 ) )
            pygame.draw.line( pygame.display.get_surface(), 'green', self.pos + App.worldOffset + pygame.Vector2( 0, -10 ), self.pos + App.worldOffset + pygame.Vector2( 0, 10 ) )
    
    def hit( self ):
        self.hp -= 1