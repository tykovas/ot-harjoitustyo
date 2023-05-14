import unittest
from synthesizer.oscillator import Oscillator
from synthesizer.synthesizer import Synthesizer
from main import Main
import numpy


class TestSynth(unittest.TestCase):
    def setUp(self):
        self.osc = Oscillator()

    def test_get_sine_returns_something(self):
        self.assertNotEqual(self.osc.get_sine(), None)

    def test_get_square_returns_something(self):
        self.assertNotEqual(self.osc.get_square(), None)

    def test_synthesizer_generate_sound_int16(self):
        self.synth = Synthesizer()
        self.gen = self.synth.generate_sound()
        assert type(self.gen[0]) is numpy.int16

    def test_oscillator_freq_change(self):
        self.osc1 = Oscillator(freq = 100)
        self.osc2 = Oscillator(freq = 1200)
        self.assertNotEqual(self.osc1.increment, self.osc2.increment)
    
    # def test_wavetofile(self):
    #     self.synth = Synthesizer()
    #     wav = self.synth.generate_sound(
    #                     440, self.synth.duration, self.synth.waveform,
    #                     self.synth.amp, self.synth.release, self.synth.attack)
    #     self.assert
