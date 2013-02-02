#!/usr/bin/env python
""" """

import pygame
from pygame.locals import *

#----------------------------------------------------------------------
class GameEngine(object):
    """ """
    def __init__(self):
        self.__running = False
        self.__fullscreen = False
        self.__states = []
        self._screensize = (0,0)
        self._screen = []
    def __del__(self): pass
    def Init(self, title, screensize, bpp=0, fullscreen=False):
        self._screensize = screensize
        pygame.init()        
        self._screen = pygame.display.set_mode(self._screensize,0,32)
        pygame.display.set_caption("Hello, World!")
        print "GameEngine init"
        self.__running = True
    def Cleanup(self):
        # Clean off state stack
        while self.__states:
            self.__states[-1].Cleanup()
            self.__states.pop()
        self._screen = pygame.display.set_mode(self._screensize,0,0)
        print "GameEngine cleanup"
        pygame.quit()
    def ChangeState(self, state):
        # Clean off state stack
        if self.__states:
            self.__states[-1].Cleanup()
            self.__states.pop()
        # store and init the new state
        self.__states.append(state)
        self.__states[-1].__init__()
    def PushState(self, state):
        # pause the current state
        if self.__states:
            self.__states[-1].Pause()
        # store and init the new state
        self.__states.append(state)
        self.__states[-1].__init__()
    def PopState(self):
        # Clean off state stack
        if self.__states:
            self.__states[-1].Cleanup()
            self.__states.pop()
        # resume the previous state
        if self.__states:
            self.__states[-1].Resume()
    def HandleEvents(self):
        # let the current state handle the event queue
        self.__states[-1].HandleEvents(self)
    def Update(self):
        # let the current state update the game
        self.__states[-1].Update(self)
    def Draw(self):
        # let the current state draw the screen
        self.__states[-1].Draw(self)
    def Running(self): return self.__running
    def Quit(self): self.__running = False
#----------------------------------------------------------------------
if __name__ == "__main__":
    print __doc__.strip()
#----------------------------------------------------------------------
