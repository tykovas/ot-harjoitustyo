import pygame as pg
import numpy as np
import pyaudio

class SoundPlayer:
    def __init__(self,soundlist):
        pg.mixer.pre_init(channels=1, allowedchanges=1)
        pg.init()
        soundarray = np.array(soundlist)
        soundarray = np.int16(soundarray* 0.1 * (2 ** 15 - 1))
        sound = pg.sndarray.make_sound(soundarray)
        sound.play()
        _running = True
        while _running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    break
        pg.quit()

        
