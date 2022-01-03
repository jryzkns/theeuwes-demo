import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import sys

from utils import *
from definitions import *

from ring import Ring

class Trial:
    def __init__(self, w, h, *config_args):
        self.canvas = pg.Surface((w, h), pg.SRCALPHA)
        self.config_args = config_args
        ring = Ring(w, h, *config_args)
        ring.draw(self.canvas)
        self.answer = pg.K_RIGHT if ring.answer == 1 else pg.K_LEFT

    def wait_key(self, timeout):
        timer, clock = 0, pg.time.Clock()
        clock.tick()
        while timer < timeout:
            handle_events()
            timer += clock.tick()
            keys = pg.key.get_pressed()
            if sum(keys) != 1:
                continue
            if keys[pg.K_ESCAPE]:
                print("EXPERIMENT ABORTED")
                sys.exit(1)
            else:
                self.rt, self.correct = timer, keys[self.answer]
                return True
        return False

    def output(self):
        return ','.join(map(str,
            [ *self.config_args[-2:], self.rt, self.correct]
            )) + '\n'

    def draw(self, surf):
        surf.blit(self.canvas, (0, 0))

if __name__ == "__main__":
    TEST_RES = (600, 600)
    pg.init()
    test_window = pg.display.set_mode(TEST_RES)
    t = Trial(*TEST_RES, 120, 5, A1)
    test_window.fill(BLACK)
    t.draw(test_window)
    pg.display.flip()
    valid = t.wait_key(1500)
    if valid:
        print(t.output())
    else:
        print("invalid input detected!")
