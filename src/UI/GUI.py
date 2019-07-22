"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""

import tkinter as tk

from typing import List

from src.Controllers.Temperature import ControllerTemperature
from src.global_variables import DOMAIN_TO_LIST, PLACEHOLDER


class GUI:
    """
    The class responsible for the GUI and all its associated functions
    """

    def __init__(self, master):
        self.master = master
        master.title("UniversalUnitConverter version 0.1")

        self.top_full_input = []
        self.bottom_full_input = []

        self.selected_domain = 'Temperature'

        # When selecting a new domain:
        self.options = DOMAIN_TO_LIST[self.selected_domain]
        #

        #
        # Minimum size config
        for x in range(5):
            self.master.grid_rowconfigure(x, minsize=50, weight=1)

        for y in range(7):
            self.master.grid_columnconfigure(y, minsize=100, weight=1)

        #
        # Placeholder
        self.placeholder_label = tk.Label(self.master, text="THIS\nIS\nA\nPLACEHOLDER\nFOR\nTHE\nUNITS\nSELECTION")
        self.placeholder_label.grid(row=0, rowspan=5, column=0, columnspan=2)

        #
        # Top TextBox
        self.top_value = tk.StringVar(self.master)
        self.top_textbox = tk.Entry(self.master, textvariable=self.top_value)
        self.top_textbox.grid(row=1, column=3)

        #
        # Top DropDown
        self.top_unit_choice = tk.StringVar(self.master)
        self.top_unit_choice.set(PLACEHOLDER)
        self.top_dropdown = tk.OptionMenu(master, self.top_unit_choice, *self.options)
        self.top_dropdown.grid(row=1, column=5)

        #
        # Equal Sign
        self.equal_sign = tk.Label(master, text="=")
        self.equal_sign.grid(row=2, column=4)

        #
        # Bottom TextBox
        self.bottom_value = tk.StringVar(self.master)
        self.bottom_textbox = tk.Entry(self.master, textvariable=self.bottom_value)
        self.bottom_textbox.grid(row=3, column=3)

        #
        # Bottom DropDown
        self.bottom_unit_choice = tk.StringVar(self.master)
        self.bottom_unit_choice.set(PLACEHOLDER)
        self.bottom_dropdown = tk.OptionMenu(master, self.bottom_unit_choice, *self.options)
        self.bottom_dropdown.grid(row=3, column=5)

    def get_input(self, is_top: bool) -> List[float and str] or None:
        """
        Returns the value and unit of one of the sides
        :param is_top: Whether we want the top values
        :return: A list containing the textbox input and the dropdown choice
        """
        if is_top:
            try:
                return [float(self.top_textbox.get()), self.top_unit_choice.get()]
            except ValueError:
                return [None, self.top_unit_choice.get()]
        else:
            try:
                return [float(self.bottom_textbox.get()), self.bottom_unit_choice.get()]
            except ValueError:
                return [None, self.bottom_unit_choice.get()]

    def update_conversion(self, is_top: bool) -> None:
        """
        Updates a conversion when the opposite one is changed by the user
        :param is_top: Whether the top is being updated (Otherwise bottom)
        :return: None
        """
        top = self.get_input(True)
        bottom = self.get_input(False)
        if is_top:
            side, opposite, opposite_value = top, bottom, self.bottom_value
        else:
            side, opposite, opposite_value = bottom, top, self.top_value
        if side[0] is not None and top[1] != PLACEHOLDER and bottom[1] != PLACEHOLDER:
            try:
                from_unit = ControllerTemperature.unit_name_to_code[side[1]]
                to_unit = ControllerTemperature.unit_name_to_code[opposite[1]]
                result = ControllerTemperature.convert(float(side[0]), from_unit, to_unit)
                opposite_value.set(str(result))
            except ValueError:
                pass

    def updated_top(self, a, b, c):
        self.update_conversion(True)

    def updated_bottom(self, a, b, c):
        self.update_conversion(False)

    def continuous_conversion(self):
        top = self.get_input(True)
        bottom = self.get_input(False)
        if top[0] is not None and top[1] != PLACEHOLDER and bottom[1] != PLACEHOLDER and top != self.top_full_input:
            print("TOP CHANGED")
            self.top_full_input = top.copy()
            try:
                from_unit = ControllerTemperature.unit_name_to_code[top[1]]
                to_unit = ControllerTemperature.unit_name_to_code[bottom[1]]
                result = ControllerTemperature.convert(float(top[0]), from_unit, to_unit)
                self.bottom_value.set(str(result))
            except ValueError:
                pass
        elif bottom[0] is not None and top[1] != PLACEHOLDER and \
                bottom[1] != PLACEHOLDER and bottom != self.bottom_full_input:
            print("BOTTOM CHANGED")
            self.bottom_full_input = bottom.copy()
            try:
                from_unit = ControllerTemperature.unit_name_to_code[bottom[1]]
                to_unit = ControllerTemperature.unit_name_to_code[top[1]]
                result = ControllerTemperature.convert(float(bottom[0]), from_unit, to_unit)
                self.top_value.set(str(result))
            except ValueError:
                pass
        self.master.after(1500, self.continuous_conversion)


root = tk.Tk()
