from src.first_task.sum_manager import SumManager


def test_main_flow():
    sum_manager = SumManager(5, 15)
    result = sum_manager.run()
    assert result == "1+2+3+4+5"

    sum_manager = SumManager(4, 46)
    result = sum_manager.run()
    assert result == "12+34"

    sum_manager = SumManager(1, 1)
    result = sum_manager.run()
    assert result == "1"

    sum_manager = SumManager(11, 19236)
    result = sum_manager.run()
    assert result == "12345+6789+101+1"

    # there is no possible way to obtain 5 from 12345 string
    sum_manager = SumManager(5, 5)
    result = sum_manager.run()
    assert not result
