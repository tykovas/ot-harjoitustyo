from oscillator import SineOscillator
from wavetofile import wave_to_file
from sound import SoundPlayer

def main():
    sine = SineOscillator(freq=440)
    osc = sine.get_oscillator()
    iter(osc)
    wav = [next(osc) for _ in range(44100*10)] 
    SoundPlayer(wav)
    # wave_to_file(wav, fname="sinewave.wav")


if __name__ == "__main__":
    print("play")
    main()

