"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""

import tkinter as tk
from typing import List

from src.Controllers.Temperature import ControllerTemperature
from src.global_variables import COLUMNSIZE, DISCORD_DARK, DISCORD_DARK_HOVER, DISCORD_LIGHT, \
    DISCORD_TEXTBOX, DOMAIN_TO_LIST, DROPDOWN_DEFAULT_TEXT, ROWSIZE


class GUI:
    """
    The class responsible for the GUI and all its associated functions
    """

    def __init__(self, master):
        self.master = master
        master.title("UniversalUnitConverter version 0.1")

        self.master.configure(bg=DISCORD_DARK)

        self.full_input = []

        self.selected_domain = 'Temperature'

        # When selecting a new domain:
        self.options = DOMAIN_TO_LIST[self.selected_domain]
        #

        #
        # Minimum size config
        for x in range(5):
            self.master.grid_rowconfigure(x, minsize=ROWSIZE[x], weight=1)

        for y in range(6):
            self.master.grid_columnconfigure(y, minsize=COLUMNSIZE[y], weight=1)

        #
        # Placeholder
        self.placeholder_label = tk.Label(
                self.master, text="THIS\nIS\nA\nPLACEHOLDER\nFOR\nTHE\nUNITS\nSELECTION",
                fg=DISCORD_LIGHT, bg=DISCORD_DARK, font=('Verdana', 36))
        self.placeholder_label.grid(row=0, rowspan=5, column=0)

        #
        # Top TextBox
        self.top_value = tk.StringVar(self.master)
        self.top_textbox = tk.Entry(self.master, textvariable=self.top_value,
                                    font=('Verdana', 24), width=7, fg=DISCORD_LIGHT,
                                    bg=DISCORD_TEXTBOX)
        self.top_textbox.grid(row=1, column=2)

        #
        # Top DropDown
        self.top_unit_choice = tk.StringVar(self.master)
        self.top_unit_choice.set(DROPDOWN_DEFAULT_TEXT)
        self.top_dropdown = tk.OptionMenu(master, self.top_unit_choice, *self.options)
        self.top_dropdown.configure(font=('Verdana', 24), fg=DISCORD_LIGHT, bg=DISCORD_DARK,
                                    highlightthickness=0, activeforeground='white',
                                    activebackground=DISCORD_DARK_HOVER)
        self.top_dropdown['menu'].configure(font=('Verdana', 24), fg=DISCORD_LIGHT, bg=DISCORD_DARK,
                                            activeforeground='white',
                                            activebackground=DISCORD_DARK_HOVER)
        self.top_dropdown.grid(row=1, column=4)

        #
        # Equal Sign
        self.equal_sign = tk.Label(master, text="=", font=('Verdana', 48), fg=DISCORD_LIGHT,
                                   bg=DISCORD_DARK)
        self.equal_sign.grid(row=2, column=3)

        #
        # Bottom TextBox
        self.bottom_value = tk.StringVar(self.master)
        self.bottom_textbox = tk.Entry(self.master, textvariable=self.bottom_value,
                                       font=('Verdana', 24), width=7, state='disabled')
        self.bottom_textbox.configure(disabledforeground=DISCORD_LIGHT,
                                      disabledbackground=DISCORD_TEXTBOX)
        self.bottom_textbox.bind("<Button-1>", self.copy_result_to_clipboard)
        self.bottom_textbox.grid(row=3, column=2)

        #
        # Bottom DropDown
        self.bottom_unit_choice = tk.StringVar(self.master)
        self.bottom_unit_choice.set(DROPDOWN_DEFAULT_TEXT)
        self.bottom_dropdown = tk.OptionMenu(master, self.bottom_unit_choice, *self.options)
        self.bottom_dropdown.configure(font=('Verdana', 24), fg=DISCORD_LIGHT, bg=DISCORD_DARK,
                                       highlightthickness=0, activeforeground='white',
                                       activebackground=DISCORD_DARK_HOVER)
        self.bottom_dropdown['menu'].configure(font=('Verdana', 24), fg=DISCORD_LIGHT,
                                               bg=DISCORD_DARK,
                                               activeforeground='white',
                                               activebackground=DISCORD_DARK_HOVER)
        self.bottom_dropdown.grid(row=3, column=4)

        self.continuous_conversion()

    def get_input(self) -> List[float and str] or None:
        """
        Returns the value and unit of the top
        :return: A list containing the textbox input and the dropdown choice
        """
        try:
            return [float(self.top_textbox.get()), self.top_unit_choice.get()]
        except ValueError:
            return [None, self.top_unit_choice.get()]

    def copy_result_to_clipboard(self, dummy) -> None:
        """
        Copies the result of the conversion to the clipboard
        This function is called whenever the bottom textbox is clicked
        :param dummy: An object returned by the click bind. Not necessary for this function
        """
        print("Text copied to clipboard")
        self.master.clipboard_clear()
        self.master.clipboard_append(self.bottom_value.get())
        self.master.update()

    def continuous_conversion(self) -> None:
        """
        Continuously monitors the top textbox and dropdown for changes (every 0.5 seconds)
        When it detects a change, it updates the bottom conversion
        """
        top = self.get_input()
        bottom_unit = self.bottom_unit_choice.get()
        if top[0] is not None and top[1] != DROPDOWN_DEFAULT_TEXT and \
                bottom_unit != DROPDOWN_DEFAULT_TEXT and [top, bottom_unit] != self.full_input:
            print("Change detected, updating result...")
            self.full_input = [top.copy(), bottom_unit]
            try:
                from_unit = ControllerTemperature.unit_name_to_code[top[1]]
                to_unit = ControllerTemperature.unit_name_to_code[bottom_unit]
                result = ControllerTemperature.convert(float(top[0]), from_unit, to_unit)
                self.bottom_value.set(str(result))
            except ValueError:
                pass
        self.master.after(500, self.continuous_conversion)


root = tk.Tk()
