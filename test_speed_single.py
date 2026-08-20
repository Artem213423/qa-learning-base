# test_speed_single.py

def check_speed(speed):
    if speed < 0:
        return "error"
    elif 0 <= speed <= 60:
        return "ok"
    else:
        return "warning"


def test_negative_speed():
    assert check_speed(-5) == "error"
    assert check_speed(-1) == "error"

def test_valid_speed():
    assert check_speed(0) == "ok"
    assert check_speed(30) == "ok"
    assert check_speed(60) == "ok"

def test_over_limit():
    assert check_speed(61) == "warning"
    assert check_speed(120) == "warning"
