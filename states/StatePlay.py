#!/usr/bin/env python
""" """

import pygame
from pygame.locals import *

from classes.states import GameState 

from states.StateMenu import StateMenu

#----------------------------------------------------------------------
class StatePlay(GameState):
    """ """
    def __init__(self):
        background_image = './assets/play.bmp'
        self.__bg = pygame.image.load(background_image).convert()
        del(background_image)
        print "PlayState Init"
    def Cleanup(self):
        # del(self.__bg)
        print "PlayState cleanup"
    def Pause(self): print "PlayState pause"
    def Resume(self): print "PlayState resume"
    def HandleEvents(self, engine):
        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            engine.Quit()
        elif event.type == KEYDOWN and event.key == K_m:
            menu=StateMenu()
            engine.PushState( menu )
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
