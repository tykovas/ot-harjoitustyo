from oscillator import sine_oscillator
from wavetofile import wave_to_file

def main():
    sine = sine_oscillator(freq=2000)
    osc = sine.get_oscillator()
    iter(osc)
    wav = [next(osc) for _ in range(44100*2)] 
    wave_to_file(wav, fname="sinewave.wav")


if __name__ == "__main__":
    print("play")
    main()

