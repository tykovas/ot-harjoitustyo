import pygame as pg
import pygame_gui as pgui
from synthesizer.synthesizer import Synthesizer
from gui.synthgui import SynthGui
from wavetofile import wave_to_file

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

key_to_note = {
    pg.K_a: "c",
    pg.K_w: "c#",
    pg.K_s: "d",
    pg.K_e: "d#",
    pg.K_d: "e",
    pg.K_f: "f",
    pg.K_t: "f#",
    pg.K_g: "g",
    pg.K_y: "g#",
    pg.K_h: "a",
    pg.K_u: "a#",
    pg.K_j: "b"
}


class GUI:
    def __init__(self):

        pg.mixer.pre_init(channels=1, allowedchanges=1)
        pg.init()
        synthgui = SynthGui()
        self.window = pg.display.set_mode(synthgui.size)
        pg.display.set_caption("Synthesizer")
        self.background = pg.Surface(synthgui.size)
        self.background.fill(pg.Color("antiquewhite"))

        self.clock = pg.time.Clock()

        self.synth = Synthesizer()
        self.synthgui = SynthGui()
        self.synthgui.button_sine.select()

        self._running = True
        while self._running:
            time_delta = self.clock.tick(60)/1000.0
            self.event()
            self.synthgui.manager.update(time_delta)

            self.window.blit(self.background, (0, 0))
            self.synthgui.manager.draw_ui(self.window)
            pg.display.update()
        pg.quit()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key in key_to_note:
                note = notes[key_to_note[event.key]]
                self.synth.play(note, self.synth.duration, self.synth.waveform,
                                self.synth.amp, self.synth.release, self.synth.attack)

            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == self.synthgui.button_square:
                    self.synth.waveform = "square"

                    self.synthgui.button_sine.unselect()
                    self.synthgui.button_square.select()

                if event.ui_element == self.synthgui.button_sine:
                    self.synth.waveform = "sine"
                    self.synthgui.button_sine.select()
                    self.synthgui.button_square.unselect()

                if event.ui_element == self.synthgui.button_save:
                    wav = self.synth.generate_sound(
                        440, self.synth.duration, self.synth.waveform,
                        self.synth.amp, self.synth.release, self.synth.attack)
                    wave_to_file(wav, self.synth.waveform + ".wav", 44100)

            if event.type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.synthgui.volume_slider:
                    self.synth.amp = self.synthgui.volume_slider.get_current_value()

                if event.ui_element == self.synthgui.duration_slider:
                    self.synth.duration = self.synthgui.duration_slider.get_current_value()

                if event.ui_element == self.synthgui.release_slider:
                    self.synth.release = self.synthgui.release_slider.get_current_value()

                if event.ui_element == self.synthgui.attack_slider:
                    self.synth.attack = self.synthgui.attack_slider.get_current_value()

            if event.type == pg.QUIT:
                self._running = False
                break

            self.synthgui.manager.process_events(event)
