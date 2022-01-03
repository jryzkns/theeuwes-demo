import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

from math import sin, cos, pi
from random import sample, uniform, randint

from utils import *
from definitions import *

class Ring:
    def __init__(self, w, h, ring_r, num_stims, type, size = 20, thickness = 5):
        self.center, self.size, self.thickness = (w//2, h//2), size, thickness
        self.ring_r, self.type = ring_r, type
        init_angle = uniform(0, 2 * pi)
        self.coords = [
            translate(
                (   ring_r * cos(init_angle + 2 * pi / num_stims * i),
                    ring_r * sin(init_angle + 2 * pi / num_stims * i)),
                *self.center)
            for i in range(num_stims)]
        self.t_idx, self.d_idx = sample(range(num_stims), 2)

        self.line_oris = [ (pi/4 + randint(0, 1) * pi/2) for _ in range(num_stims)]
        self.answer, _ = divmod(self.line_oris[self.t_idx], pi/2)

    def draw(self, surf):
        for idx, (coord, orientation) in enumerate(zip(self.coords, self.line_oris)):
            pg.draw.line(   surf,
                            WHITE,
                            translate(coord,  *scale(sincos(orientation),  self.size//2)),
                            translate(coord,  *scale(sincos(orientation), -self.size//2)),
                            int(self.thickness * 0.6))
            if self.type == A1:
                if idx == self.t_idx:
                    pg.draw.circle(surf, GREEN, coord, self.size, self.thickness)
                else:
                    pg.draw.polygon(surf, GREEN, diamond_coords(coord, self.size), self.thickness)
            elif self.type == A2:
                if idx == self.t_idx:
                    pg.draw.circle(surf, GREEN, coord, self.size, self.thickness)
                elif idx == self.d_idx:
                    pg.draw.polygon(surf, RED, diamond_coords(coord, self.size), self.thickness)
                else:
                    pg.draw.polygon(surf, GREEN, diamond_coords(coord, self.size), self.thickness)
            elif self.type == B1:
                if idx == self.t_idx:
                    pg.draw.circle(surf, GREEN, coord, self.size, self.thickness)
                else:
                    pg.draw.circle(surf, RED, coord, self.size, self.thickness)
            elif self.type == B2:
                if idx == self.t_idx:
                    pg.draw.circle(surf, GREEN, coord, self.size, self.thickness)
                elif idx == self.d_idx:
                    pg.draw.polygon(surf, RED, diamond_coords(coord, self.size), self.thickness)
                else:
                    pg.draw.circle(surf, RED, coord, self.size, self.thickness)

if __name__ == '__main__':
    TEST_RES = (600, 600)
    pg.init()
    test_window = pg.display.set_mode(TEST_RES)
    ring = Ring(*TEST_RES, 120, 7, B2)
    while True:
        handle_events()
        ring.draw(test_window)
        pg.display.flip()
