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
            if value < -459.67:
                raise ValueError("Temperature under absolute 0!")
            return round((value - 32) * 5 / 9, 2)
        elif unit == "c":
            if value < -273.15:
                raise ValueError("Temperature under absolute 0!")
            return round(value * 9 / 5 + 32, 2)
        else:
            raise ValueError("Wrong unit given!")

    @staticmethod
    def celsius_and_kelvin(value: float, unit: str) -> float:
        """
        Converts between celsius and kelvin
        :param value: input value
        :param unit: input unit (c,k)
        :return: The conversion in the other unit
        :raises ValueError: if unit is invalid
        """
        if unit == "k":
            if value < 0:
                raise ValueError("Temperature under absolute 0!")
            return round(value - 273.15, 2)
        elif unit == "c":
            if value < -273.15:
                raise ValueError("Temperature under absolute 0!")
            return round(value + 273.15, 2)
        else:
            raise ValueError("Wrong unit given!")

    @staticmethod
    def fahrenheit_and_kelvin(value: float, unit: str) -> float:
        """
        Converts between fahrenheit and kelvin
        :param value: input value
        :param unit: input unit (f, k)
        :return: The conversion in the other unit
        :raises ValueError: if unit is invalid
        """
        if unit == "f":
            if value < -459.67:
                raise ValueError("Temperature under absolute 0!")
            return round((value + 459.67) * 5 / 9, 2)
        elif unit == "k":
            if value < 0:
                raise ValueError("Temperature under absolute 0!")
            return round((value * 9 / 5) - 459.67, 2)
        else:
            raise ValueError("Wrong unit given!")