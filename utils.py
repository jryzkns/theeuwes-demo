from math import sin, cos
import pygame as pg
import sys

def translate(p, dx, dy):
    px, py = p
    return px + dx, py + dy

def scale(p, s):
    px, py = p
    return px * s, py * s

def sincos(orientation):
    return sin(orientation), cos(orientation)

def diamond_coords(p, r):
    return (
        translate(p,  r,  0),
        translate(p,  0, -r),
        translate(p, -r,  0),
        translate(p,  0,  r),
    )

def handle_events():
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()

def get_time_now():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
