#!/usr/bin/env python
""" """

import pygame
from pygame.locals import *

#----------------------------------------------------------------------
class GameState(object):
    """ """
    def Init(self): pass
    def Cleanup(self): pass
    def Pause(self): pass
    def Resume(self): pass
    def HandleEvents(self, engine): pass
    def Update(self, engine): pass
    def Draw(self, engine): pass
    def ChangeState(self, engine, state): engine.ChangeState(state)
#----------------------------------------------------------------------
if __name__ == "__main__":
    print __doc__.strip()
#----------------------------------------------------------------------
