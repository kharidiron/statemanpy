#!/usr/bin/env python
""" """

import pygame
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
TEAL = (0,255,255)
LIGHTGREY = (191,191,191)
GREY = (127,127,127)
DARKGREY = (63,63,63)

#----------------------------------------------------------------------
class StateMenu(object):
    """ """
    def __init__(self):
        self._screensize = (640,480)
        pygame.init()

        self._screen = pygame.display.set_mode(self._screensize, 0, 32)
        pygame.display.set_caption("test")

        self._bg = pygame.Surface(self._screensize)
        self._bg.fill(DARKGREY)

        self.font = pygame.font.SysFont("arial", 20)
        self.menu = []
        self.menupos = []

        self.menu_poet = [('Robert Penn Warren', 'self.menu_warren'), ('Edger Allen Poe','self.menu_poe')]
        self.menu_warren = [('We live in time so little time',None), ('And we learn all so painfully',None), ('That we may spare this hour\'s term',None), ('To practice for eternity.',None),('Back','back')]
        self.menu_poe = [('O God! can I not save',None), ('One from the pitiless wave?',None), ('Is all that we see or seem',None), ('But a dream within a dream?',None),('Back','back')]

        self.selected = 0
        self.textpos = []
        self.decorated_menu_text = []

        self.menu.append('self.menu_poet')
        self.menupos.append(self.selected)
    def Cleanup(self):
        print "MenuState cleanup"
    def Pause(self):
        print "MenuState pause"
    def Resume(self):
        print "MenuState resume"
    def HandleEvents(self):
        event = pygame.event.poll()
        if event.type == QUIT:
            # engine.Quit()
            exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            # engine.PopState( )
            exit()
        #####vv
        elif event.type == KEYDOWN and event.key == pygame.K_UP:
            self.highlighter(-1)
        elif event.type == KEYDOWN and event.key == pygame.K_DOWN:
            self.highlighter(+1)
        elif event.type == KEYDOWN and event.key == pygame.K_RETURN:
            self.selector()
        #####^^
        else:
            pass
    def Update(self):
        #####vv
        self.textpos, self.decorated_menu_text = self.menu_builder()
        #####^^
    def Draw(self):
        self._screen.blit(self._bg, (0,0))
        #####vv
        for index, text in enumerate(self.decorated_menu_text):
            self._screen.blit( text , self.textpos[index] )
        #####^^
        pygame.display.update()
#----------------------------------------------------------------------
    #####vvvv
    def highlighter(self, selector):
        selected = self.selected
        selected += selector
        if selected < 0:
            selected = len(eval(self.menu[-1])) - 1
        elif selected >= len(eval(self.menu[-1])):
            selected = 0
        self.selected = selected
    def selector(self):
        if eval(self.menu[-1])[self.selected][1] == None:
            pass
        elif eval(self.menu[-1])[self.selected][1] == 'back':
            self.menu.pop()
            self.selected = self.menupos[-1]
            self.menupos.pop()
        else:
            self.menu.append(eval(self.menu[-1])[self.selected][1])
            self.menupos.append(self.selected)
            self.selected = 0
    def menu_builder(self):
        menu_text = eval(self.menu[-1])

        decorated_menu_text = []
        xs = ys = []

        idx_longest = menu_text.index(max(menu_text, key=lambda x: len(x[0])))
        menuheight = len(menu_text)*self.font.get_linesize()
        topset = (self._screensize[1] - menuheight)/2
        y = topset - self.font.get_linesize()
        for index, [text, link] in enumerate(menu_text):
            if index == self.selected:
                decorated_menu_text.append(self.font.render(text, True, YELLOW))
            else:
                decorated_menu_text.append(self.font.render(text, True, WHITE))
            ys.append(y)
            if index == idx_longest:
                x = decorated_menu_text[index].get_rect(centerx=self._screensize[0]/2)
            y += self.font.get_linesize()
        xs = [x[0]] * len(menu_text)
        textpos = zip(xs, ys)
        return (textpos, decorated_menu_text)
        #####^^^^
#----------------------------------------------------------------------
def main():
    """ """
    menu = StateMenu()
    while True:
        menu.HandleEvents()
        menu.Update()
        menu.Draw()
    menu.Cleanup()
    pygame.quit()
#----------------------------------------------------------------------
if __name__ == "__main__":
    main()
#----------------------------------------------------------------------
