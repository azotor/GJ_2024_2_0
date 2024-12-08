import pygame
import App

class Keys:
    def __init__( self ):
        self.controller = None

    def update( self ):
        keys = pygame.key.get_pressed()
        
        if self.controller == None and pygame.joystick.get_count() :
            self.controller = pygame.joystick.Joystick( 0 )
            self.controller.init()
        
        if self.controller:

            keyMap.A = True if self.controller.get_button( 0 ) == 1 else False
            keyMap.B = True if self.controller.get_button( 1 ) == 1 else False

            axiesIntense = .2

            if self.controller.get_numaxes and self.controller.get_numhats:
                dpad = self.controller.get_hat( 0 )
                keyMap.LEFT = True if self.controller.get_axis( 0 ) < -axiesIntense or dpad[ 0 ] == -1 else False
                keyMap.UP = True if self.controller.get_axis( 1 ) < -axiesIntense or dpad[ 1 ] == 1 else False
                keyMap.RIGHT = True if self.controller.get_axis( 0 ) > axiesIntense or dpad[ 0 ] == 1 else False
                keyMap.DOWN = True if self.controller.get_axis( 1 ) > axiesIntense or dpad[ 1 ] == -1 else False
            elif self.controller.get_numaxes:
                keyMap.LEFT = True if self.controller.get_axis( 0 ) < -axiesIntense else False
                keyMap.UP = True if self.controller.get_axis( 1 ) < -axiesIntense else False
                keyMap.RIGHT = True if self.controller.get_axis( 0 ) > axiesIntense else False
                keyMap.DOWN = True if self.controller.get_axis( 1 ) > axiesIntense else False
            elif self.controller.get_numhats:
                dpad = self.controller.get_hat( 0 )
                keyMap.LEFT = True if dpad[ 0 ] == -1 else False
                keyMap.UP = True if dpad[ 1 ] == 1 else False
                keyMap.RIGHT = True if dpad[ 0 ] == 1 else False
                keyMap.DOWN = True if dpad[ 1 ] == -1 else False

class KeyMap:
    LEFT = False
    UP = False
    RIGHT = False
    DOWN = False
    A = False
    B = False

keyMap = KeyMap()

keys = Keys()