import Config

class Cooldown:
    def __init__( self, timer = 0 ):
        self.timer = timer
        self.timeCounter = 0
        self.running = False

    def setTimer( self, timer ):
        self.timer = timer
    
    def start( self ):
        self.running = True

    def stop( self ):
        self.running = False
    
    def update( self ):
        if self.running:
            self.timeCounter += 1000 / Config.App.FPS
            if self.timeCounter >= self.timer:
                self.running = False
                self.timeCounter = 0