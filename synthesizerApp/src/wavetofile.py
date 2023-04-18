import numpy as np
from scipy.io import wavfile

def wave_to_file(wav, fname="temp.wav", amp=0.1, sample_rate=44100):
    wav = np.array(wav)
    wav = np.int16(wav* amp * (2 ** 15 - 1))
    wavfile.write(fname, sample_rate, wav)