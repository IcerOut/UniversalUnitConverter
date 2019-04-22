"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""

import tkinter as tk

# from Controllers.Temperature import ControllerTemperature
from global_variables import DOMAIN_TO_LIST

class GUI:
    """
    The class responsible for the GUI and all its associated functions
    """

    def __init__(self, master):
        self.master = master
        master.title("UniversalUnitConverter version 0.1")
        self.selected_domain = 'Temperature'

        # When selecting a new domain:
        self.options = DOMAIN_TO_LIST[self.selected_domain]
        #

        #
        # Minimum size config
        for x in range(5):
            self.master.grid_rowconfigure(x, minsize=100, weight=1)

        for y in range(7):
            self.master.grid_columnconfigure(y, minsize=150, weight=1)

        #
        # Placeholder
        self.placeholder_label = tk.Label(self.master, text="THIS\nIS\nA\nPLACEHOLDER\nFOR\nTHE\nUNITS\nSELECTION")
        self.placeholder_label.grid(row=0, rowspan=5, column=0, columnspan=2)

        #
        # Top TextBox
        self.top_textbox = tk.Entry(self.master)
        self.top_textbox.grid(row=1, column=3)

        #
        # Top DropDown
        self.top_unit_choice = tk.StringVar(self.master)
        self.top_unit_choice.set('Choose a unit:')
        self.top_dropdown = tk.OptionMenu(master, self.top_unit_choice, *self.options)
        self.top_dropdown.grid(row=1, column=5)

        #
        # Equal Sign
        self.equal_sign = tk.Label(master, text="=")
        self.equal_sign.grid(row=2, column=4)

        #
        # Bottom TextBox
        self.bottom_textbox = tk.Entry(self.master)
        self.bottom_textbox.grid(row=3, column=3)

        #
        # Top DropDown
        self.bottom_unit_choice = tk.StringVar(self.master)
        self.bottom_unit_choice.set('Choose a unit:')
        self.bottom_dropdown = tk.OptionMenu(master, self.bottom_unit_choice, *self.options)
        self.bottom_dropdown.grid(row=3, column=5)


root = tk.Tk()
