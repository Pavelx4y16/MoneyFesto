from typing import List


def validate_init_arguments(cls):
    """This is class decorator.
    The main goal is to run validation function ("__validate_init_arguments"),
       which should be created in every class if we want to use this decorator.
    This decorator simplifies call to the validation method, increases readability and reduces code duplications
    Example of usage:

      @validate_init_arguments
      class Person:
        def __validate_init_arguments(self, name, age=25):
            assert isinstance(name, str)
            assert isinstance(age, int)

        def __init__(self, name, age=25):
            self.name = name
            self.age = age

    As we see from example: all you need, just to mark your class with '@validate_init_arguments'
       and implement corresponding validation function.

    Notes: 1) signatures of validation function and __init__ should be identical (including default parameters)
           2) decorated class can be safely inherited, because the identical method naming problem is resolved by
                usage of private ("__*") methods. That means, validation function will not be overriden by
                Child's validation function.
    """
    original_init = cls.__init__

    def decorated_init(self, *args, **kwargs):
        validate = getattr(self, f"_{cls.__name__}__validate_init_arguments")
        validate(*args, **kwargs)
        original_init(self, *args, **kwargs)

    cls.__init__ = decorated_init

    return cls


@validate_init_arguments
class MonotonicSequenceFinder:
    def __validate_init_arguments(self, sequence):
        assert isinstance(sequence, list) and sequence and all(isinstance(item, int) for item in sequence)

    def __init__(self, sequence: List[int]):
        self.sequence = sequence
        self.sequence_number = len(sequence)

    def find_next(self, start_position, check_monotonic):
        """Finds length of strictly monotonic sequence"""
        position = start_position + 1
        while position < self.sequence_number and check_monotonic(self.sequence[position-1], self.sequence[position]):
            position += 1

        return position - start_position

    def run(self, check_monotonic):
        current_max = (0, 1)
        start_position = 0
        while start_position < self.sequence_number:
            monotonic_seq_length = self.find_next(start_position, check_monotonic)
            end_position = start_position + monotonic_seq_length

            if monotonic_seq_length > current_max[1] - current_max[0]:
                current_max = (start_position, end_position)
            start_position = end_position

        return current_max[0], current_max[1] - 1


if __name__ == "__main__":
    sequence = list(map(int, input().split(',')))

    finder = MonotonicSequenceFinder(sequence)

    max_increasing_sequence = finder.run(lambda x, y: x > y)
    max_decreasing_sequence = finder.run(lambda x, y: x < y)

    max_increasing_sequence_length = max_increasing_sequence[1] - max_increasing_sequence[0]
    max_decreasing_sequence_length = max_decreasing_sequence[1] - max_decreasing_sequence[0]

    result = max_decreasing_sequence
    if (max_increasing_sequence_length > max_decreasing_sequence_length) or \
            (max_increasing_sequence_length == max_decreasing_sequence_length and
                max_increasing_sequence[0] < max_decreasing_sequence[0]):
        result = max_increasing_sequence

    print(f"{result[0]}, {result[1]}")
