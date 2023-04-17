import pygame
import numpy as np
import pyaudio

class SoundPlayer:
    def __init__(self,soundlist):
        stream = pyaudio.PyAudio().open(
            rate=44100, channels=1,format=pyaudio.paInt16, output=True,frames_per_buffer=256
        )
        soundarray = np.array(soundlist)
        soundarray = np.int16(soundarray* 0.1 * (2 ** 15 - 1))
        stream.write(soundarray)
