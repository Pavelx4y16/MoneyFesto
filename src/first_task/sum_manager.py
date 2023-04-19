from src.first_task.sum_item import SumItem
from src.utils import validate_init_arguments


@validate_init_arguments
class SumManager:
    def __validate_init_arguments(self, n, required_sum):
        assert isinstance(n, int) and isinstance(required_sum, int)

    def __init__(self, n, required_sum):
        self.n = n
        self.max_number_length = len(str(required_sum))
        self.required_sum = required_sum
        self.initial_string = "".join([str(i) for i in range(1, n + 1)])
        initial_sum_item = SumItem(self.initial_string)
        self.sum_items = [initial_sum_item] + initial_sum_item.create_initial_sum_items()

    @property
    def current_sum(self):
        return sum(self.sum_items)

    @property
    def result(self):
        return "+".join(map(str, self.sum_items))

    def run(self):
        while self.sum_items:
            current_sum = self.current_sum
            if current_sum == self.required_sum:
                return self.result

            last_item = self.sum_items[-1]
            incremented = last_item.increment(self.required_sum - current_sum)
            while not incremented:
                del self.sum_items[-1]
                if self.sum_items:
                    last_item = self.sum_items[-1]
                    incremented = last_item.increment(self.required_sum - self.current_sum)
                else:
                    break

            if self.sum_items:
                self.sum_items += last_item.create_initial_sum_items()

        return self.result
