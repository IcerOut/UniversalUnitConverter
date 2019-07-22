"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""
from src.UnitConverters.Temperature import Temperature


class ControllerTemperature:
    """
    The class responsible for all temperature conversions
    It calls the appropriate function from UnitConverters depending on desired output
    """

    code_to_unit_name = {'c': '°C', 'f': '°F', 'k': 'K'}
    unit_name_to_code = {'°C': 'c', '°F': 'f', 'K': 'k'}

    @staticmethod
    def convert(value: float, input_unit: str, output_unit: str) -> float:
        """
        Converts the given value from the input unit to the output unit and returns the result
        :param value: The given temperature
        :param input_unit: The unit used in the input
        :param output_unit: The desired unit
        :return: A float representing the conversion in the desired output unit
        :raises ValueError: if either of the units is invalid or the given temperature
                            is below absolute zero
        """
        if input_unit == output_unit:
            return round(value, 2)

        converter = {
            ('f', 'c'): [Temperature.celsius_and_fahrenheit, value, 'f'],
            ('c', 'f'): [Temperature.celsius_and_fahrenheit, value, 'c'],
            ('c', 'k'): [Temperature.celsius_and_kelvin, value, 'c'],
            ('k', 'c'): [Temperature.celsius_and_kelvin, value, 'k'],
            ('f', 'k'): [Temperature.fahrenheit_and_kelvin, value, 'f'],
            ('k', 'f'): [Temperature.fahrenheit_and_kelvin, value, 'k']
            }
        if (input_unit, output_unit) in converter:
            function_with_params = converter[(input_unit, output_unit)]
            return round(function_with_params[0](function_with_params[1], function_with_params[2]),
                         2)
        raise ValueError("Invalid units given!")
