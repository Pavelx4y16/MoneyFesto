from src.first_task.sum_manager import SumManager

if __name__ == "__main__":
    n, m = map(int, input().split())

    sum_manager = SumManager(n, m)
    result = sum_manager.run()

    if not result:
        print(f"There is no possible way to obtain {m} from '{''.join([str(i) for i in range(1, n+1)])}'")
    else:
        print(result)
