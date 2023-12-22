import datetime
import json


class String:
    def __init__(self, max_length: int = 255) -> None:
        self.max_length = max_length

    def parse(self, string: str):
        return string[0 : self.max_length]


class Integer:
    def __init__(self) -> None:
        pass

    def parse(self, integer: str):
        if type(integer) is int:
            return integer
        return int(integer)


class Float:
    def __init__(self, max_length_decimal: int = -1) -> None:
        self.max_length_decimal = max_length_decimal

    def parse(self, float_number: str):
        if type(float_number) is float:
            float_number = str(float_number)

        if "," in float_number:
            float_number = float_number.replace(".", "")
            float_number = float_number.replace(",", ".")

        float_number = float(float_number)

        if self.max_length_decimal is not -1:
            float_number = float(round(float_number, self.max_length_decimal))

        return float_number


class Bool:
    def __init__(self) -> None:
        pass

    def parse(self, bool_value: str):
        if type(bool_value) is bool:
            return bool_value
        if bool_value.lower() == "true":
            return True
        return False


class DateTime:
    def __init__(self, format: str) -> None:
        self.format = format

    def parse(self, date: str):
        return datetime.datetime.strptime(date, self.format)


class Date:
    def __init__(self, format: str) -> None:
        self.format = format

    def parse(self, date: str):
        return datetime.datetime.strptime(date, self.format).date()


class Json:
    def __init__(self) -> None:
        pass

    def parse(self, json_data: str):
        if type(json_data) is dict:
            return json_data
        return json.loads(json_data)


class List:
    def __init__(self) -> None:
        pass

    def parse(self, list_data: str):
        if type(list_data) is list:
            return list_data
        return json.loads(list_data)
