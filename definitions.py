import sys
from os.path import abspath, join
HERE = abspath(".")
try:
    BASE_PATH = sys._MEIPASS
except Exception:
    BASE_PATH = abspath(".")

here = lambda fn : join(BASE_PATH, fn)
asset = lambda fn : join(BASE_PATH, 'assets', fn)

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)

A1, A2, B1, B2 = 0, 2, 1, 3

BLOCK_SIZE = 50
