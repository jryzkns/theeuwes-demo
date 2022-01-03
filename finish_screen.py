import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
from definitions import *
from utils import *

def finish_screen(surf):
    endtext = pg.image.load(asset('end.png'))
    while True:
        handle_events()
        surf.fill(BLACK)
        surf.blit(endtext,
            translate(  scale(surf.get_size(),    1/2),
                       *scale(endtext.get_size(), -1/2)))
        pg.display.flip()

if __name__ == "__main__":
    TEST_RES = (600, 600)
    pg.init()
    test_window = pg.display.set_mode(TEST_RES)
    finish_screen(test_window)
