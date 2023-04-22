import pygame as pg
import numpy as np
from synthesizer.oscillator import Oscillator


class Synthesizer:
    def __init__(self):
        pg.mixer.pre_init(channels=1, allowedchanges=1)
        pg.init()
        # self.sound = pg.sndarray.make_sound(np.empty(1, np.int16))

    def generate_sound(self, freq=440, duration=2, waveform="square"):
        sound = Oscillator(freq)
        if waveform == "sine":
            osc = sound.get_sine()
        if waveform == "square":
            osc = sound.get_square()
        iter(osc)
        self.sustain = 20000
        wav = [next(osc) for _ in range(44100*int(duration))]
        # print(wav)
        fadeoutarray = np.array(np.linspace(1,0,self.sustain))
        wav = np.array(wav)
        wav = np.int16(wav * 0.1 * (2 ** 15 - 1))

        tmp = np.int16(wav[wav.size-self.sustain:] * fadeoutarray) # sustain length fadeout array
        # print(fadeoutarray)
        # print(np.size(tmp))
        # print(type(wav))
        wav = np.concatenate((wav[:wav.size-self.sustain],tmp))
        # print(np.size(wav))
        return wav

    def output_sound(self, wav):
        self.sound = pg.sndarray.make_sound(wav)
        self.sound.play()

    def play(self, freq, duration, waveform):
        wav = self.generate_sound(freq, duration, waveform)
        self.output_sound(wav)

    def stop(self):
        self.sound.stop()

 