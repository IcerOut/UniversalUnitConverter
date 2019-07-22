"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""

import unittest

from src.Controllers.Temperature import ControllerTemperature
from src.UnitConverters.Temperature import Temperature


class TemperatureTest(unittest.TestCase):
    def test_celsius_and_fahrenheit(self):
        # int celsius to fahrenheit
        self.assertEqual(Temperature.celsius_and_fahrenheit(20, "c"), 68)
        # float celsius to fahrenheit
        self.assertEqual(Temperature.celsius_and_fahrenheit(50.3, "c"), 122.54)
        # int fahrenheit to celsius
        self.assertEqual(Temperature.celsius_and_fahrenheit(68, "f"), 20)
        # float fahrenheit to celsius
        self.assertEqual(Temperature.celsius_and_fahrenheit(122.54, "f"), 50.3)

    def test_celsius_and_kelvin(self):
        # int celsius to kelvin
        self.assertEqual(Temperature.celsius_and_kelvin(20, "c"), 293.15)
        # float celsius to kelvin
        self.assertEqual(Temperature.celsius_and_kelvin(-72.82, "c"), 200.33)
        # int kelvin to celsius
        self.assertEqual(Temperature.celsius_and_kelvin(293.15, "k"), 20)
        # float kelvin to celsius
        self.assertEqual(Temperature.celsius_and_kelvin(200.33, "k"), -72.82)

    def test_fahrenheit_and_kelvin(self):
        # int fahrenheit to kelvin
        self.assertEqual(Temperature.fahrenheit_and_kelvin(80.33, "f"), 300)
        # float fahrenheit to kelvin
        self.assertEqual(Temperature.fahrenheit_and_kelvin(-62.77, "f"), 220.5)
        # int kelvin to fahrenheit
        self.assertEqual(Temperature.fahrenheit_and_kelvin(300, "k"), 80.33)
        # float kelvin to fahrenheit
        self.assertEqual(Temperature.fahrenheit_and_kelvin(220.5, "k"), -62.77)

    def test_controller(self):
        # int celsius to fahrenheit
        self.assertEqual(ControllerTemperature.convert(20, 'c', 'f'), 68)
        # int fahrenheit to celsius
        self.assertEqual(ControllerTemperature.convert(68, 'f', 'c'), 20)
        # int celsius to kelvin
        self.assertEqual(ControllerTemperature.convert(20, 'c', 'k'), 293.15)
        # int kelvin to celsius
        self.assertEqual(ControllerTemperature.convert(293.15, 'k', 'c'), 20)
        # int fahrenheit to kelvin
        self.assertEqual(ControllerTemperature.convert(80.33, 'f', 'k'), 300)
        # int kelvin to fahrenheit
        self.assertEqual(ControllerTemperature.convert(300, 'k', 'f'), 80.33)


if __name__ == '__main__':
    unittest.main()
