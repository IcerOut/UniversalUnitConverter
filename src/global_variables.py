"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""
# Windows Titlebar Title
from src.Controllers.Distance import ControllerDistance
from src.Controllers.Temperature import ControllerTemperature

APP_TITLE = 'UniversalUnitConverter version 0.1'

# Windows Titlebar Icon (location relative to main.py)
APP_ICON = 'img\\UUC.ico'

# Rows: Free FirstRow Equal SecondRow Free
ROWSIZE = [30, 50, 30, 50, 30]

# Columns: Placeholder Free Textboxes Equal Dropdowns Free
COLUMNSIZE = [350, 30, 100, 50, 100, 30]

DROPDOWN_DEFAULT_TEXT = 'Choose a unit:'

DOMAIN_TO_LIST = {
    'Temperature': ['°C', '°F', 'K'],
    'Distance': ['Kilometers', 'Miles', 'Nautical Miles', 'Feet', 'Meters', 'Yards', 'Inches']
    }

DOMAIN_TO_CONTROLLER = {
    'Temperature': ControllerTemperature,
    'Distance': ControllerDistance
    }

DISCORD_DARK = '#2c2f33'

DISCORD_DARK_HOVER = '#23272a'

DISCORD_LIGHT = '#99aab5'

DISCORD_TEXTBOX = '#323539'
