import pygame as pg
from synthesizer.synthesizer import Synthesizer

notes = {
    "c": 261.6,
    "c#": 277.2,
    "d": 293.7,
    "d#": 311.1,
    "e": 329.6,
    "f": 349.2,
    "f#": 370,
    "g": 392,
    "g#": 415.3,
    "a": 440,
    "a#": 466.2,
    "b": 493.9
}


class GUI:
    def __init__(self):
        self.size = (400, 400)
        pg.mixer.pre_init(channels=1, allowedchanges=1)

        pg.init()
        pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self.synth = Synthesizer()
        self.waveform = "sine"
        self.duration = 1
        self._running = True
        while self._running:
            self.event()
        pg.quit()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.synth.play(notes["c"], self.duration, self.waveform)
                if event.key == pg.K_w:
                    self.synth.play(notes["c#"], self.duration, self.waveform)
                if event.key == pg.K_s:
                    self.synth.play(notes["d"], self.duration, self.waveform)
                if event.key == pg.K_e:
                    self.synth.play(notes["d#"], self.duration, self.waveform)
                if event.key == pg.K_d:
                    self.synth.play(notes["e"], self.duration, self.waveform)
                if event.key == pg.K_f:
                    self.synth.play(notes["f"], self.duration, self.waveform)
                if event.key == pg.K_t:
                    self.synth.play(notes["f#"], self.duration, self.waveform)
                if event.key == pg.K_g:
                    self.synth.play(notes["g"], self.duration, self.waveform)
                if event.key == pg.K_y:
                    self.synth.play(notes["g#"], self.duration, self.waveform)
                if event.key == pg.K_h:
                    self.synth.play(notes["a"], self.duration, self.waveform)
                if event.key == pg.K_u:
                    self.synth.play(notes["a#"], self.duration, self.waveform)
                if event.key == pg.K_j:
                    self.synth.play(notes["b"], self.duration, self.waveform)

            if event.type == pg.QUIT:
                self._running = False
                break
