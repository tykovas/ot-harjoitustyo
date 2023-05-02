import unittest
from synthesizer.oscillator import Oscillator
from synthesizer.synthesizer import Synthesizer
from main import Main
import numpy


class TestSynth(unittest.TestCase):
    def setUp(self):
        self.osc = Oscillator()

    def test_get_osc_returns_something(self):
        self.assertNotEqual(self.osc.get_sine(), None)

    def test_synthesizer_generate_sound_int16(self):
        self.synth = Synthesizer()
        self.gen = self.synth.generate_sound()
        assert type(self.gen[0]) is numpy.int16

    def test_main_start(self):
        self.run = Main()
        self.assertNotEqual(self.run.gui.synth, None)
