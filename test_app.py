from app import calculate_bmi


def test_valid_input():
    weight = 65
    height = 1.75
    result = calculate_bmi(weight, height)
    assert result == 21.22


def test_zero_height():
    weight = 65
    height = 0
    result = calculate_bmi(weight, height)
    assert result == 0.0


def test_zero_weight():
    weight = 0
    height = 1.75
    result = calculate_bmi(weight, height)
    assert result == 0.0


def test_negative_weight():
    weight = -65
    height = 1.75
    result = calculate_bmi(weight, height)
    assert result == -21.22


def test_negative_height():
    weight = 65
    height = -1.75
    result = calculate_bmi(weight, height)
    assert result == -21.22
