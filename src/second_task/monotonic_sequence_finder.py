from typing import List

from src.utils import validate_init_arguments


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
