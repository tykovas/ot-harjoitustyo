from gui.gui import GUI


class Main:
    """ Luokka, joka käynnistää ohjelman

    Attributes: 
        gui: ohjelman visuaalinen käyttöliittymä 
    """

    def __init__(self):
        """ Luokan konstruktori, joka alustaa käyttöliittymän

        Args: 
            gui: käyttöliittymä
        """
        self.gui = GUI()


if __name__ == "__main__":
    print("Pressing a-j on the keyboard will result in playback of a sinewave")
    Main()
