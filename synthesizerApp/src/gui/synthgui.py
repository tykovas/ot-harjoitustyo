import pygame as pg
import pygame_gui as pgui

class SynthGui: 
    def __init__(self):
        # self.hello_button = pgui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)),
        #                                      text='Say Hello',
        #                                      manager=self.manager)
        self.size = (800, 400)
        self.manager = pgui.UIManager(self.size)


        # Buttons
        self.button_square = pgui.elements.UIButton(relative_rect=pg.Rect((30, 50), (100, 50)),
                                               text='square',
                                               manager=self.manager)
        self.button_sine = pgui.elements.UIButton(relative_rect=pg.Rect((30, 100), (100, 50)),
                                               text='sine',
                                               manager=self.manager)