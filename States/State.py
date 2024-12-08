import App

class State:
    def __init__( self ):
        pass

    def postinit( self ):
        pass

    def changeState( self, state ):
        App.statesManager.change( state )

    def enter( self ):
        pass

    def update( self ):
        pass

    def render( self ):
        pass