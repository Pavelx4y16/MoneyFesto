from src.first_task.sum_item import SumItem
from src.utils import validate_init_arguments


@validate_init_arguments
class SumManager:
    def __validate_init_arguments(self, n, required_sum):
        assert isinstance(n, int) and isinstance(required_sum, int)

    def __init__(self, n, required_sum):
        self.n = n
        self.required_sum = required_sum
        self.initial_string = "".join([str(i) for i in range(1, n + 1)])
        self.sum_items = [SumItem(self.initial_string[i:]) for i in range(len(self.initial_string))]
        self.current_sum = sum(self.sum_items)

    def run(self):
        return NotImplemented


if __name__ == "__main__":
    manager = SumManager(5, 15)
    pass
