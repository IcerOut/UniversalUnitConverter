"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""
from src.UniversalUnitConverter.src.UnitConverters.Distance import Distance


class ControllerDistance:
    """
    The class responsible for all temperature conversions
    It calls the appropriate function from UnitConverters depending on desired output
    """

    # code_to_unit_name = {'c': '°C', 'f': '°F', 'k': 'K'}
    # unit_name_to_code = {'°C': 'c', '°F': 'f', 'K': 'k'}

    @staticmethod
    def convert(value: float, input_unit: str, output_unit: str) -> float:
        """
        Converts the given value from the input unit to the output unit and returns the result
        :param value: The given distance
        :param input_unit: The unit used in the input
        :param output_unit: The desired unit
        :return: A float representing the conversion in the desired output unit
        :raises ValueError: if either of the units is invalid or the given temperature is below absolute zero
        """
        if input_unit == output_unit:
            return round(value, 2)

        converter = {
            ("km", "mi"): [Distance.kilometer_and_mile, value, "km"],
            ("mi", "km"): [Distance.kilometer_and_mile, value, "mi"],
            ("mi", "nmi"): [Distance.mile_and_nautical_mile, value, "mi"],
            ("mi", "nmi"): [Distance.mile_and_nautical_mile, value, "nmi"],
            ("km", "nmi"): [Distance.kilometer_and_nautical_mile, value, "km"],
            ("nmi", "km"): [Distance.kilometer_and_nautical_mile, value, "nmi"],
            ("m", "ft"): [Distance.foot_to_meter, value, "m"],
            ("ft", "m"): [Distance.foot_to_meter, value, "ft"],
            ("m", "yd"): [Distance.yard_to_meter, value, "m"],
            ("yd", "m"): [Distance.yard_to_meter, value, "yd"],
            ("cm", "in"): [Distance.centimeter_to_inch, value, "cm"],
            ("in", "cm"): [Distance.centimeter_to_inch, value, "in"],
            ("ft", "yd"): [Distance.foot_to_yard, value, "ft"],
            ("yd", "ft"): [Distance.foot_to_yard, value, "yd"],
            ("ft", "in"): [Distance.foot_to_inch, value, "ft"],
            ("in", "ft"): [Distance.foot_to_inch, value, "in"],
            ("mi", "ft"): [Distance.mile_and_foot, value, "mi"],
            ("ft", "mi"): [Distance.mile_and_foot, value, "ft"],
            ("mi", "yd"): [Distance.mile_and_yard, value, "mi"],
            ("yd", "mi"): [Distance.mile_and_yard, value, "yd"],
            ("mi", "in"): [Distance.mile_and_inch, value, "mi"],
            ("in", "mi"): [Distance.mile_and_inch, value, "in"],
            ("yd", "in"): [Distance.inch_to_yard, value, "yd"],
            ("in", "yd"): [Distance.inch_to_yard, value, "in"],

        }
        if (input_unit, output_unit) in converter:
            function_with_params = converter[(input_unit, output_unit)]
            return function_with_params[0](function_with_params[1], function_with_params[2])
        raise ValueError("Invalid units given!")
