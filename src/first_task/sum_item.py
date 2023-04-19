from src.utils import validate_init_arguments


@validate_init_arguments
class SumItem:
    def __validate_init_arguments(self, raw_string):
        assert isinstance(raw_string, str)

    def __init__(self, raw_string: str):
        self.raw_string = raw_string
        self.current_number_length = 1

    def __add__(self, number: int):
        return int(self.raw_string[:self.current_number_length]) + number

    def __radd__(self, number: int):
        return self + number

    def increment(self):
        self.current_number_length += 1
        return self.current_number_length <= len(self.raw_string)

    def create_initial_sum_items(self):
        """Creates the rest of SumItems with number_length == 1, while it is possible."""
        raw_string = self.raw_string[self.current_number_length:]
        return [SumItem(raw_string[i:]) for i in range(len(raw_string))]

    def __repr__(self):
        return self.raw_string[:self.current_number_length]
