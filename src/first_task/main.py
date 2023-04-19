from src.first_task.sum_manager import SumManager

if __name__ == "__main__":
    n, m = input().split()
    print(n, m)
    sum_manager = SumManager(int(n), int(m))
    sum_manager.run()
    result = sum_manager.get_result()
    print(result)