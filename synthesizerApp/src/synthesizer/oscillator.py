import math
import itertools
import numpy as np


class Oscillator:
    def __init__(self, freq=1000, sample_rate=44100):
        self._freq = freq
        self._sample_rate = sample_rate
        self.increment = (2 * np.pi * self._freq)/self._sample_rate

    def get_sine(self):
        self.sine = (np.sin(v) for v in itertools.count(start=0, step=self.increment))
        return self.sine

    def get_square(self):
        self.square =(np.sign(np.sin(v)) for v in itertools.count(start=0, step=self.increment))
        return self.square    
