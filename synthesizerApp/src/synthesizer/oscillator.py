import math
import itertools
import numpy as np


class SineOscillator:
    def __init__(self, freq=1000, sample_rate=44100):
        self._freq = freq
        self._sample_rate = sample_rate

    def get_oscillator(self):
        increment = (2 * np.pi * self._freq)/self._sample_rate
        sine = (math.sin(v) for v in itertools.count(start=0, step=increment))
        return sine
