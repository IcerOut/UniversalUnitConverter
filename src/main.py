"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""
from src.UI.GUI import GUI, root

if __name__ == '__main__':
    my_gui = GUI(root)
    # my_gui.continuous_conversion()
    # my_gui.top_value.trace('w', my_gui.updated_top)
    # my_gui.bottom_value.trace('w', my_gui.updated_bottom)
    my_gui.master.mainloop()
