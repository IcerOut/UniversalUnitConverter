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


if __name__ == '__main__':
    unittest.main()
