import pygame as pg
import numpy as np
from synthesizer.oscillator import Oscillator


class Synthesizer:
    def __init__(self):
        pg.mixer.pre_init(channels=1, allowedchanges=1)
        pg.init()


    def generate_sound(self, freq=440, duration=2, waveform="sine", amp=0.5, release = 0):
        sound = Oscillator(freq)
        
        if waveform == "sine":
            osc = sound.get_sine()
        if waveform == "square":
            osc = sound.get_square()
        iter(osc)
        wav = [next(osc) for _ in range(44100*int(duration))]



        wav = np.array(wav)
        release = int(wav.size*release)
        # release = 20000
        fadeoutarray = np.array(np.linspace(1,0,release))

        amp = amp * 0.1
        print(release)
        wav = np.int16(wav * amp * (2 ** 15 - 1))
        print(wav.size)
        print(release)
        tmp = np.int16(wav[wav.size-release:] * fadeoutarray) # sustain length fadeout array
        wav = np.concatenate((wav[:wav.size-release],tmp))
        return wav

    def output_sound(self, wav):
        self.sound = pg.sndarray.make_sound(wav)
        self.sound.play()

    def play(self, freq, duration, waveform, amp, release):
        wav = self.generate_sound(freq, duration, waveform, amp, release)
        self.output_sound(wav)

    def stop(self):
        self.sound.stop()

 