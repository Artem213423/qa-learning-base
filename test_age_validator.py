ages = [17,18,65,66]
def check_age(age: int) -> bool:
    return 18 <= age <= 65


def test_age_below_boundary():
    assert check_age(17) is False


def test_age_lower_boundary():
    assert check_age(18) is True


def test_age_upper_boundary():
    assert check_age(65) is True


def test_age_above_boundary():
    assert check_age(66) is False