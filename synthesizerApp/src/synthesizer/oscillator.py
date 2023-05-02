import itertools
import numpy as np


class Oscillator:
    """Luokka, joka luo generaattorit ääniaaltojen muodostamista varten.

    Attributes: 
        freq: Luotavan ääniaallon taajuus
        sample_rate: Synteesissä käyttetävien samplejen määrä sekunnissa. 
        increment: Samplejen "ajallinen" etäisyys toisistaan

    """
    def __init__(self, freq=1000, sample_rate=44100):
        """Luokan konstruktori, joka alustaa uuden oskillaattorin
        
        Args: 
            freq: Luotavan ääniaallon taajuus
            sample_rate: Synteesissä käyttetävien samplejen määrä sekunnissa. 
        """
        self.freq = freq
        self.sample_rate = sample_rate
        self.increment = (2 * np.pi * self._freq)/self._sample_rate

    def get_sine(self):
        """Palauttaa siniaalto generaattorin määritellyllä inkrementillä
        Returns: 
            siniaalto -generaattori"""
        sine = (np.sin(v)
                     for v in itertools.count(start=0, step=self.increment))
        return sine

    def get_square(self):
        """Palauttaa kanttiaalto generaattorin määritellyllä inkrementillä
        Returns: 
            kanttiaalto -generaattori
        """
        square = (np.sign(np.sin(v))
                       for v in itertools.count(start=0, step=self.increment))
        return square
