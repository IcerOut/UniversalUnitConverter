"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""


class Temperature:
    @staticmethod
    def celsius_and_fahrenheit(value: float, unit: str) -> float:
        """
        Converts between celsius and fahrenheit
        :param value: input value
        :param unit: input unit (c,f)
        :return: The conversion in the other unit
        :raises ValueError: if unit is invalid
        """
        if unit == "f":
            return round((value - 32) * 5 / 9, 2)
        elif unit == "c":
            return round(value * 9 / 5 + 32, 2)
        else:
            raise ValueError("Wrong unit given!")
