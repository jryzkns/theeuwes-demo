import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from time import sleep
from random import shuffle

import pygame as pg
pg.init()

from definitions import *
from utils import *

from fixation import Fixation
from trial import Trial

screen_info = pg.display.Info()
RES = ( screen_info.current_w,
        screen_info.current_h)

from demographics import get_demographic_fn
FN = here(f'{get_demographic_fn()}-{get_time_now()}.csv')
with open(FN, 'w+') as f__:
    f__.write("num_stims,trial_type,RT,correct\n")

fcross = Fixation(*RES)
beep = pg.mixer.Sound(asset('beep.ogg'))
pg.mouse.set_visible(False)

exp_win = pg.display.set_mode(RES, pg.FULLSCREEN)

from breakperiod import break_screen
def trial_generator():
    arg_types_list = [ (num_stims, trial_type)
                        for num_stims in [5, 7, 9]
                        for trial_type in [A1, A2, B1, B2]
                        for _ in range(5) ]
    shuffle(arg_types_list)
    for idx, arg_types in enumerate(arg_types_list, 1):
        if idx % BLOCK_SIZE == 0:
            break_screen(exp_win)
        yield Trial(*RES, 120, *arg_types)

from tutorial import tutorial_screen
tutorial_screen(exp_win)

trials = trial_generator()
for trial in trials:
    handle_events()

    exp_win.fill(BLACK)

    fcross.draw(exp_win)
    pg.display.flip()
    sleep(1)

    trial.draw(exp_win)
    pg.display.flip()

    valid = trial.wait_key(1500)

    if valid:
        with open(FN, 'a+') as f__:
            f__.write(trial.output())
    else:
        beep.play()

    exp_win.fill(BLACK)
    fcross.draw(exp_win)
    pg.display.flip()

    sleep(1)

from resmailer import mailout_results
mailout_results((FN,), dest='xza194@sfu.ca')

from finish_screen import *
finish_screen(exp_win)
