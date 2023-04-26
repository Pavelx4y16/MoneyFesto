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


if __name__ == "__main__":
    n, m = map(int, input().split())

    sum_manager = SumManager(n, m)
    result = sum_manager.run()

    if not result:
        print(f"There is no possible way to obtain {m} from '{sum_manager.initial_string}'")
    else:
        print(f"{result}={m}")
