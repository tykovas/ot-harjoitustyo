import pygame as pg
import pygame_gui as pgui

class SynthGui: 
    def __init__(self):
        self.size = (800, 400)
        self.manager = pgui.UIManager(self.size)


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
        self.duration_text = pgui.elements.UITextBox("Duration",relative_rect=(pg.Rect((30, 200), (100, 30))),manager=self.manager)




        self.duration_slider = pgui.elements.UIHorizontalSlider(relative_rect=(pg.Rect((30,230),(200,40))),start_value=2,value_range=(1,5),manager=self.manager)

        self.release_slider = pgui.elements.UIHorizontalSlider(relative_rect=(pg.Rect((30,280),(200,40))),start_value=0.5,value_range=(0,1),manager=self.manager)