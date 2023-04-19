from src.first_task.sum_manager import SumManager

if __name__ == "__main__":
    n, m = map(int, input().split())

    sum_manager = SumManager(n, m)
    result = sum_manager.run()

    if not result:
        print(f"There is no possible way to obtain {m} from '{sum_manager.initial_string}'")
    else:
        print(f"{result}={m}")
