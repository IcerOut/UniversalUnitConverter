"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""

from UnitConverters.Temperature import Temperature
import unittest


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


if __name__ == '__main__':
    unittest.main()
