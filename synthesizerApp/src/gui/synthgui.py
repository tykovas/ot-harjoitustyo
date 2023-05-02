import pygame as pg
import pygame_gui as pgui


class SynthGui:
    def __init__(self):
        """Luokka, joka vastaa käyttöliittymän visuaalisten elementtien luomisesta

        Attributes: 
            size: Luotavan ikkunan koko
            manager: pygame_gui:n käyttämä UIManager moduuli
            button_(square/sine): nappi, jolla käyttäjä voi valita käyttämänsä aaltomuodon
            button_save: nappi, jolla käyttäjä voi tallentaa muodostamansa 
                ääniaallon wav-tiedostoksi
            (volume/duration/release/attack)_slider: Liukusäädin, jolla käyttäjä voi hallita 
                Synth-luokan amp,duration,attack ja release -arvoja
            (...)_text: Käyttöliittymään piirrettävän ohjetekstit
        """
        self.size = (800, 400)
        self.manager = pgui.UIManager(self.size)

        # Buttons
        self.button_square = pgui.elements.UIButton(relative_rect=pg.Rect((30, 50), (100, 50)),
                                                    text='square',
                                                    manager=self.manager)
        self.button_sine = pgui.elements.UIButton(relative_rect=pg.Rect((30, 100), (100, 50)),
                                                  text='sine',
                                                  manager=self.manager)

        self.button_save = pgui.elements.UIButton(relative_rect=pg.Rect((660, 300), (100, 50)),
                                                  text='save',
                                                  manager=self.manager)

        # Sliders
        self.volume_slider = pgui.elements.UIHorizontalSlider(relative_rect=(pg.Rect(
            (500, 50), (200, 40))), start_value=0.5, value_range=(0, 1), manager=self.manager)

        self.duration_slider = pgui.elements.UIHorizontalSlider(relative_rect=(pg.Rect(
            (30, 230), (200, 40))), start_value=1.5, value_range=(0.1, 4), manager=self.manager)

        self.release_slider = pgui.elements.UIHorizontalSlider(relative_rect=(pg.Rect(
            (30, 310), (200, 40))), start_value=0.1, value_range=(0, 1), manager=self.manager)
        self.attack_slider = pgui.elements.UIHorizontalSlider(relative_rect=(pg.Rect(
            (240, 310), (200, 40))), start_value=0.1, value_range=(0, 1), manager=self.manager)

        # Text
        self.volume_text = pgui.elements.UITextBox("Volume", relative_rect=(
            pg.Rect((500, 20), (200, 30))), manager=self.manager)
        self.waveform_text = pgui.elements.UITextBox("Waveform", relative_rect=(
            pg.Rect((30, 20), (100, 30))), manager=self.manager)
        self.duration_text = pgui.elements.UITextBox("Length", relative_rect=(
            pg.Rect((30, 200), (100, 30))), manager=self.manager)
        self.duration_text = pgui.elements.UITextBox("Release", relative_rect=(
            pg.Rect((30, 280), (100, 30))), manager=self.manager)
        self.attack_text = pgui.elements.UITextBox("Attack", relative_rect=(
            pg.Rect((240, 280), (100, 30))), manager=self.manager)
