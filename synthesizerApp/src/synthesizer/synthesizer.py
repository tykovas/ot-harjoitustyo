import pygame as pg
import numpy as np
from synthesizer.oscillator import Oscillator


class Synthesizer:
    """Luokka, joka vastaa syntetisaattorin äänen tuottamisesta ja toistamisesta

    Attributes: 
        waveform: toistettavan äänen ääniaalto
        duration: toistettavan äänen pituus sekuntteina
        amp: soitettavan äänen äänenvoimakkuus välillä 0-1
        attack: Nopeus jolla ääni syttyy täyteen äänenvoimakkuuteen
        relese: Nopeus jolla ääni sammuu

    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa syntetisaattorin
        """
        pg.mixer.pre_init(channels=1, allowedchanges=1)
        pg.init()
        self.waveform = "sine"
        self.duration = 1
        self.amp = 0.5
        self.attack = 0.1
        self.release = 0.1

    def generate_sound(self, freq=440, duration=2, waveform="sine",
                       amp=0.5, release=0.1, attack=0.1):
        """Muodostaa Oscillator luokan palauttaman generaattorin pohjalta arrayn
        jonka avulla haluttu ääniaalto saadaan soitettua. 

        Muodostaa tarvittaessa (riippuen release ja attack -arvoista) fadeout ja fadein -arrayt 
        joilla äänen syttymis ja sammumis nopeutta voidaan hallita. 

        Args: 
            freq: Äänen taajuus
            duration: Äänen kokonaiskesto sekunteina
            waveform : Äänen aaltomuoto
            amp: Äänenvoimakkuuden taso
            release: Äänen sammumisnopeus
            attack: Äänen syttymisnopeus

        Returns: 
            numpy array joka kuvaa haluttua ääniaaltoa

        """
        sound = Oscillator(freq)

        if waveform == "sine":
            osc = sound.get_sine()
        if waveform == "square":
            osc = sound.get_square()
        iter(osc)
        wav = [next(osc) for _ in range(int(44100*(duration)))]
        wav = np.array(wav)

        release = int(wav.size*release)
        attack = int(wav.size*attack)

        fadeoutarray = np.array(np.linspace(1, 0, release))
        fadeinarray = np.array(np.linspace(0, 1, attack))

        amp = amp * 0.1

        wav = np.int16(wav * amp * (2 ** 15 - 1))
        # sustain length fadeout array
        tmp = np.int16(wav[wav.size-release:] * fadeoutarray)
        tmpattack = np.int16(fadeinarray * wav[:attack])

        wav = np.concatenate((wav[:wav.size-release], tmp))
        wav = np.concatenate((tmpattack, wav[attack:]))

        return wav

    def output_sound(self, wav):
        """Muodostaa pygamen sndarrayn, joka toistetaan käyttäjän äänentoistolaitteistosta

        Args: 
            wav: array joka halutaan toistaa
        """
        sound = pg.sndarray.make_sound(wav)
        sound.play()

    def play(self, freq, duration, waveform, amp, release, attack):
        """Muodostaa generate_sound metodin avulla toistettavan arrayn
        ja antaa sen output_sound arraylle toistettavaksi

        Args: 
            freq: Äänen taajuus
            duration: Äänen kokonaiskesto sekunteina
            waveform : Äänen aaltomuoto
            amp: Äänenvoimakkuuden taso
            release: Äänen sammumisnopeus
            attack: Äänen syttymisnopeus
        """
        wav = self.generate_sound(
            freq, duration, waveform, amp, release, attack)
        self.output_sound(wav)

    # def stop(self):
    #     sound.stop()
