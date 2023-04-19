from src.second_task.monotonic_sequence_finder import MonotonicSequenceFinder


if __name__ == "__main__":
    sequence = list(map(int, input().split(',')))

    finder = MonotonicSequenceFinder(sequence)

    max_increasing_sequence = finder.run(lambda x, y: x > y)
    max_decreasing_sequence = finder.run(lambda x, y: x < y)

    result = max_decreasing_sequence
    if max_increasing_sequence[1] - max_increasing_sequence[0] > max_decreasing_sequence[1] - max_decreasing_sequence[0]:
        result = max_increasing_sequence

    print(f"{result[0]}, {result[1]}")
