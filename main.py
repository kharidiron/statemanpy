#!/usr/bin/env python
""" """

import pygame
from pygame.locals import *

from classes.engine import GameEngine 
from states.StateIntro import StateIntro

#----------------------------------------------------------------------
def main():
    """ """
    game = GameEngine()
    screensize = (640,480)
    game.Init('An Init Title', screensize)
    intro = StateIntro()
    game.ChangeState( intro )
    while game.Running():
        game.HandleEvents()
        game.Update()
        game.Draw()
    game.Cleanup()
#----------------------------------------------------------------------
if __name__ == "__main__":
    main()
#----------------------------------------------------------------------
