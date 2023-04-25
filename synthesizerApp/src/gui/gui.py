import pygame as pg
from synthesizer.synthesizer import Synthesizer
from gui.synthgui import SynthGui
import pygame_gui as pgui 

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

        self.waveform = "sine"
        self.duration = 1
        self.amp = 0.5

        




        self._running = True
        while self._running:
            time_delta = self.clock.tick(60)/1000.0
            self.event()
            self.synthgui.manager.update(time_delta)
            
            self.window.blit(self.background,(0,0))
            self.synthgui.manager.draw_ui(self.window)
            pg.display.update()
        pg.quit()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.synth.play(notes["c"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_w:
                    self.synth.play(notes["c#"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_s:
                    self.synth.play(notes["d"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_e:
                    self.synth.play(notes["d#"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_d:
                    self.synth.play(notes["e"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_f:
                    self.synth.play(notes["f"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_t:
                    self.synth.play(notes["f#"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_g:
                    self.synth.play(notes["g"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_y:
                    self.synth.play(notes["g#"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_h:
                    self.synth.play(notes["a"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_u:
                    self.synth.play(notes["a#"], self.duration, self.waveform, self.amp)
                if event.key == pg.K_j:
                    self.synth.play(notes["b"], self.duration, self.waveform, self.amp)

            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == self.synthgui.button_square:
                    self.waveform = "square"
                    
                    self.synthgui.button_sine.unselect()
                    self.synthgui.button_square.select()
                    
                if event.ui_element == self.synthgui.button_sine:
                    self.waveform = "sine"
                    self.synthgui.button_sine.select()
                    self.synthgui.button_square.unselect()

            if event.type == pgui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == self.synthgui.volume_slider:
                    self.amp = self.synthgui.volume_slider.get_current_value()

            if event.type == pg.QUIT:
                self._running = False
                break

            self.synthgui.manager.process_events(event)
