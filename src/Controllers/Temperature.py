"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""
from UnitConverters.Temperature import Temperature


class ControllerTemperature:
    """
    The class responsible for all temperature conversions
    It calls the appropriate function from UnitConverters depending on desired output
    """

    @staticmethod
    def convert(value: float, input_unit: str, output_unit: str) -> float:
        """
        Converts the given value from the input unit to the output unit and returns the result
        :param value: The given temperature
        :param input_unit: The unit used in the input
        :param output_unit: The desired unit
        :return: A float representing the conversion in the desired output unit
        :raises ValueError: if either of the units is invalid or the given temperature is below absolute zero
        """
        if input_unit == output_unit:
            return round(value, 2)

        converter = {
            ('f', 'c'): Temperature.celsius_and_fahrenheit(value, 'f'),
            ('c', 'f'): Temperature.celsius_and_fahrenheit(value, 'c'),
            ('c', 'k'): Temperature.celsius_and_kelvin(value, 'c'),
            ('k', 'c'): Temperature.celsius_and_kelvin(value, 'k'),
            ('f', 'k'): Temperature.fahrenheit_and_kelvin(value, 'f'),
            ('k', 'f'): Temperature.fahrenheit_and_kelvin(value, 'k')
            }
        if (input_unit, output_unit) in converter:
            return converter[(input_unit, output_unit)]
        raise ValueError("Invalid units given!")
