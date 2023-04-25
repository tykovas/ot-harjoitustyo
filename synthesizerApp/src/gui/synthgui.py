import pygame as pg
import pygame_gui as pgui

class SynthGui: 
    def __init__(self):
        # self.hello_button = pgui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)),
        #                                      text='Say Hello',
        #                                      manager=self.manager)
        self.size = (800, 400)
        self.manager = pgui.UIManager(self.size, r'\gui\button.json')


        # Buttons
        self.button_square = pgui.elements.UIButton(relative_rect=pg.Rect((30, 50), (100, 50)),
                                               text='square',
                                               manager=self.manager)
        self.button_sine = pgui.elements.UIButton(relative_rect=pg.Rect((30, 100), (100, 50)),
                                               text='sine',
                                               manager=self.manager)    
        


        # Volume slider
        self.volume_slider = pgui.elements.UIHorizontalSlider(relative_rect=(pg.Rect((500,50),(200,40))),start_value=0.5,value_range=(0,1),manager=self.manager)


        # Text
        self.volume_text = pgui.elements.UITextBox("Volume",relative_rect=(pg.Rect((500,20),(200,30))),manager=self.manager)
        self.waveform_text = pgui.elements.UITextBox("Waveform",relative_rect=(pg.Rect((30, 20), (100, 30))),manager=self.manager)