"""

UniversalUnitConverter
@author: Lung Alin-Sebastian
@author: Lisca Alexandru Iosif

"""


class Distance:
    @staticmethod
    def kilometer_and_mile(value: float, unit: str) -> float:
        if unit == "km":  # convert to mile
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 0.62137
        elif unit == "mi":  # convert to km
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 0.62137

    @staticmethod
    def centimeter_to_inch(value: float, unit: str) -> float:
        if unit == "cm":  # convert to inch
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 2.54
        elif unit == "in":  # convert to centimeter
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 2.54

    @staticmethod
    def foot_to_meter(value: float, unit: str) -> float:
        if unit == "m":  # convert to foot
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 3.28084
        elif unit == "ft":  # convert to centimeter
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 3.28084

    @staticmethod
    def yard_to_meter(value: float, unit: str) -> float:
        if unit == "m":  # convert to yard
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 1.0936
        elif unit == "yd":  # convert to centimeter
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 1.0936

    @staticmethod
    # international
    def kilometer_and_nautical_mile(value: float, unit: str) -> float:
        if unit == "km":  # convert to nautical mile
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 0.539957
        elif unit == "nmi":  # convert to km
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 0.539957

    @staticmethod
    def mile_and_nautical_mile(value: float, unit: str) -> float:
        if unit == "mi":  # convert to nautical mile
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 0.87
        elif unit == "nmi":  # convert to mile
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 0.87

    @staticmethod
    def mile_and_yard(value: float, unit: str) -> float:
        if unit == "mi":  # convert to yard
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 1760
        elif unit == "yd":  # convert to mile
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 1760

    @staticmethod
    def mile_and_foot(value: float, unit: str) -> float:
        if unit == "mi":  # convert to foot
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 5280
        elif unit == "ft":  # convert to mile
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 5280

    @staticmethod
    def mile_and_inch(value: float, unit: str) -> float:
        if unit == "mi":  # convert to inch
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 63360
        elif unit == "in":  # convert to mile
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 63360

    @staticmethod
    def foot_to_inch(value: float, unit: str) -> float:
        if unit == "ft":  # convert to inch
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 12
        elif unit == "in":  # convert to feet
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 12

    @staticmethod
    def foot_to_yard(value: float, unit: str) -> float:
        if unit == "ft":  # convert to yard
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 0.3333334
        elif unit == "yd":  # convert to feet
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 0.3333334

    @staticmethod
    def inch_to_yard(value: float, unit: str) -> float:
        if unit == "in":  # convert to yard
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value * 0.0277778
        elif unit == "yd":  # convert to inch
            if value < 0:
                raise ValueError("Distance cannot be lower than 0!")
            return value / 0.0277778
