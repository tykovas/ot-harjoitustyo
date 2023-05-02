from scipy.io import wavfile


def wave_to_file(wav, fname="temp.wav", sample_rate=44100):
    """
    Funktio tallettaa annetun ääniaallon wav-tiedostona hakemistoon
    """
    wavfile.write(fname, sample_rate, wav)
