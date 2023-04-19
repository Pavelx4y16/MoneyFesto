from src.utils import validate_init_arguments


@validate_init_arguments
class SumItem:
    def __validate_init_arguments(self, raw_string):
        assert isinstance(raw_string, str)

    def __init__(self, raw_string: str):
        self.raw_string = raw_string
        self.current_string_length = 1

    def __add__(self, number: int):
        return int(self.raw_string[:self.current_string_length]) + number

    def __radd__(self, number: int):
        return self + number
