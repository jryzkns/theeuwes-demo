import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

from definitions import *
from utils import *

class Fixation:
    def __init__(self, w, h, size = 5, width = 3):
        self.center, self.size, self.width = (w//2, h//2), size, width
        self.N = translate(self.center,          0,  self.size)
        self.E = translate(self.center,  self.size,          0)
        self.S = translate(self.center,          0, -self.size)
        self.W = translate(self.center, -self.size,          0)

    def draw(self, surf):
        pg.draw.line(surf, WHITE, self.W, self.E, self.width)
        pg.draw.line(surf, WHITE, self.S, self.N, self.width)

if __name__ == "__main__":
    TEST_RES = (200, 200)
    pg.init()
    test_window = pg.display.set_mode(TEST_RES)
    fcross = Fixation(*TEST_RES)
    while True:
        handle_events()
        fcross.draw(test_window)
        pg.display.flip()
