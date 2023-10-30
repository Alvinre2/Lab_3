import Lab2.Lab2 as Lab2


def test_calc_average():
    numbers = [64, 34, 25]
    result = Lab2.calc_average(numbers)
    assert result == 41.0


def test_calc_min_max():
    numbers = [64, 34, 25]
    result = Lab2.calc_min_max(numbers)
    assert result == [25, 64]


def test_calc_median_odd():
    numbers = [5, 67, 32]
    result = Lab2.calc_median(numbers)
    assert result == 32.0


def test_calc_median_even():
    numbers = [5, 67, 32, 10]
    result = Lab2.calc_median(numbers)
    assert result == 21.0

