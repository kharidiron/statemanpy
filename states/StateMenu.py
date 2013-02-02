#!/usr/bin/env python
""" """

import pygame
from pygame.locals import *

from classes.states import GameState 

#----------------------------------------------------------------------
class StateMenu(GameState):
    """ """
    def __init__(self):
        background_image = './assets/menu.bmp'
        self.__bg = pygame.image.load(background_image).convert()
        del(background_image)
        print "MenuState Init"
    def Cleanup(self):
        # del(self.__bg)
        print "MenuState cleanup"
    def Pause(self): print "MenuState pause"
    def Resume(self): print "MenuState resume"
    def HandleEvents(self, engine):
        event = pygame.event.poll()
        if event.type == QUIT:
            engine.Quit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            engine.PopState( )
        else:
            pass
    def Update(self, engine): pass
    def Draw(self, engine):
        engine._screen.blit(self.__bg, (0,0))
        pygame.display.update()
#----------------------------------------------------------------------
if __name__ == "__main__":
    print __doc__.strip()
#----------------------------------------------------------------------
