from synthesizer.oscillator import SineOscillator
import pygame as pg
import numpy as np
 

class Synthesizer:
    def __init__(self):
        pg.mixer.pre_init(channels=1, allowedchanges=1)
        pg.init()
        self.sound = pg.sndarray.make_sound(np.empty(1,np.int16))


    def generate_sound(self, freq=440, duration=2, waveform="sine"):
        
        if waveform == "sine":
            sound = SineOscillator(freq)
        osc = sound.get_oscillator()
        iter(osc)
        wav = [next(osc) for _ in range(44100*int(duration))] 
        wav = np.array(wav)
        wav = np.int16(wav* 0.1 * (2 ** 15 - 1))
        return wav

    def output_sound(self, wav):
        self.sound = pg.sndarray.make_sound(wav)
        self.sound.play()  

    def play(self, freq, duration, waveform):
        wav = self.generate_sound(freq, duration, waveform)
        self.output_sound(wav)

    def stop(self):
        self.sound.stop()