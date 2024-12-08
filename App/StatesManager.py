import States

class StatesManager:
    def __init__( self ):
        self.states = {
            'PRELOAD' : States.Preload(),
            'MAIN' : States.Main(),
            'PLAY' : States.Play()
        }

        self.currentState = None
        self.change( 'PRELOAD' )
    
    def postinit( self ):
        for state in self.states.values():
            state.postinit()

    def change( self, state ):
        self.currentState = self.states[ state ]
        self.currentState.enter()

    def update( self ):
        self.currentState.update()
    
    def render( self ):
        self.currentState.render()