import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
from definitions import *
from utils import *

def break_screen(surf):
    breaktext = pg.image.load(asset('break.png'))
    while True:
        handle_events()
        if pg.key.get_pressed()[pg.K_SPACE]:
            break
        surf.fill(BLACK)
        surf.blit(breaktext,
            translate(  scale(surf.get_size(),    1/2),
                       *scale(breaktext.get_size(), -1/2)))
        pg.display.flip()

if __name__ == '__main__':
    TEST_RES = (600, 600)
    pg.init()
    test_window = pg.display.set_mode(TEST_RES)
    break_screen(test_window)
