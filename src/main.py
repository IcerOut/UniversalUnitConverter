"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""
from UI.GUI import GUI, root

if __name__ == '__main__':
    my_gui = GUI(root)
    my_gui.check_input()
    my_gui.master.mainloop()
