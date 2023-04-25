import pygame as pg
import numpy as np
from synthesizer.oscillator import Oscillator


class Synthesizer:
    def __init__(self):
        pg.mixer.pre_init(channels=1, allowedchanges=1)
        pg.init()

    def generate_sound(self, freq=440, duration=2, waveform="square", amp=0.5):
        sound = Oscillator(freq)
        if waveform == "sine":
            osc = sound.get_sine()
        if waveform == "square":
            osc = sound.get_square()
        iter(osc)
        self.sustain = 20000
        wav = [next(osc) for _ in range(44100*int(duration))]
        fadeoutarray = np.array(np.linspace(1,0,self.sustain))
        wav = np.array(wav)
        amp = amp * 0.1
        wav = np.int16(wav * amp * (2 ** 15 - 1))

        tmp = np.int16(wav[wav.size-self.sustain:] * fadeoutarray) # sustain length fadeout array
        wav = np.concatenate((wav[:wav.size-self.sustain],tmp))
        return wav

    def output_sound(self, wav):
        self.sound = pg.sndarray.make_sound(wav)
        self.sound.play()

    def play(self, freq, duration, waveform, amp):
        wav = self.generate_sound(freq, duration, waveform, amp)
        self.output_sound(wav)

    def stop(self):
        self.sound.stop()

 