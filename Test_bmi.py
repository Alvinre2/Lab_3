
import Lab2.bmi as bmi


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73, 60)
    correct_result = 0
    assert (result==correct_result)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73, 100)
    correct_result = 1
    assert (result == correct_result)


def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73, 30)
    correct_result = -1
    assert (result == correct_result)



