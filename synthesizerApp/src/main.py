from oscillator import sine_oscillator
from wavetofile import wave_to_file

sine = sine_oscillator()
osc = sine.get_oscillator()
iter(osc)
wav = [next(osc) for _ in range(44100*2)] 
wave_to_file(wav, fname="sinewave.wav")



