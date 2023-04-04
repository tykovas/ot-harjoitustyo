import unittest 
from oscillator import sine_oscillator
# from main import main

class TestSynth(unittest.TestCase):
    def setUp(self):
        self.osc = sine_oscillator()

    def test_get_osc_returns_something(self):
        self.assertNotEqual(self.osc.get_oscillator(),None)


