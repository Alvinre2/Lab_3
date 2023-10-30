import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_sort_more_than_10():
    input_arr = [10, 20, 45, 23, 14, 63, 80, 31, 50, 67, 24]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 1)


def test_bubble_sort_non_integer():
    input_arr = [64, 34, "25", 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 2


def test_bubble_sort_empty():
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 0  # REQ-04: Return 0 for an empty list