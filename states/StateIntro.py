#!/usr/bin/env python
""" """

import pygame
from pygame.locals import *

from classes.states import GameState 

from states.StatePlay import StatePlay

#----------------------------------------------------------------------
class StateIntro(GameState):
    """ """
    def __init__(self):
        background_image = './assets/intro.bmp'
        self.__bg = pygame.image.load(background_image).convert()
        del(background_image)
        self.__alpha = 254
        self.__fader = pygame.Surface(self.__bg.get_size())
        self.__fader.fill((0,0,0,self.__alpha))
        print "IntroState Init"
    def Cleanup(self):
        # del(self.__bg)
        print "IntroState cleanup"
    def Pause(self): print "IntroState pause"
    def Resume(self): print "IntroState resume"
    def HandleEvents(self, engine):
        event = pygame.event.poll()
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            engine.Quit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            play=StatePlay()
            engine.ChangeState( play )
        else:
            pass
    def Update(self, engine):
        self.__alpha -= 2
        if self.__alpha < 0:
            self.__alpha = 0
        self.__fader.set_alpha(self.__alpha)
    def Draw(self, engine):
        engine._screen.blit(self.__bg, (0,0))
        if self.__alpha != 0:
            engine._screen.blit(self.__fader, (0,0))
        pygame.display.update()
#----------------------------------------------------------------------
if __name__ == "__main__":
    print __doc__.strip()
#----------------------------------------------------------------------
    