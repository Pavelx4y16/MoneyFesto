from src.utils import validate_init_arguments


@validate_init_arguments
class SumItem:
    def __validate_init_arguments(self, raw_string):
        assert isinstance(raw_string, str)

    def __init__(self, raw_string: str):
        self.raw_string = raw_string
        self.current_number_length = 1

    @property
    def number(self):
        return int(self.raw_string[:self.current_number_length])

    def __add__(self, number: int):
        return self.number + number

    def __radd__(self, number: int):
        return self + number

    def increment(self, rest_sum: int):
        if self.current_number_length + 1 > len(self.raw_string):
            return False

        rest_sum += self.number
        self.current_number_length += 1
        # this number will be recalculated based on incremented self.current_number_length
        rest_sum -= self.number

        return rest_sum >= 0

    def create_initial_sum_items(self):
        """Creates the rest of SumItems with number_length == 1, while it is possible."""
        raw_string = self.raw_string[self.current_number_length:]
        return [SumItem(raw_string[i:]) for i in range(len(raw_string))]

    def __repr__(self):
        return self.raw_string[:self.current_number_length]
