from src.second_task.monotonic_sequence_finder import MonotonicSequenceFinder


def _test_finder(sequence, expected_result):
    finder = MonotonicSequenceFinder(sequence)

    max_increasing_sequence = finder.run(lambda x, y: x > y)
    max_decreasing_sequence = finder.run(lambda x, y: x < y)

    result = max_decreasing_sequence
    if max_increasing_sequence[1] - max_increasing_sequence[0] > max_decreasing_sequence[1] - max_decreasing_sequence[0]:
        result = max_increasing_sequence

    assert result == expected_result


def test_finder():
    _test_finder([-3, 2, 3, 4, 5, 6, 7, 7, 8], (0, 6))
    _test_finder([-1, -1, -1, -1, -1, -1, -1, -1, -1], (0, 0))
    _test_finder([-1], (0, 0))
    _test_finder([1, 2, 3], (0, 2))
    _test_finder([1, 2, 3, 2, 1, 0], (2, 5))
    _test_finder([5, 1, 2, 3, 4, 5, 2, 1, 0], (1, 5))
