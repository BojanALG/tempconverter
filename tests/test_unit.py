from converter import celsius_to_fahrenheit

def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32.0

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212.0

def test_twenty_degrees():
    assert celsius_to_fahrenheit(20) == 68.0

def test_minus_forty_is_equal():
    assert celsius_to_fahrenheit(-40) == -40.0

def test_decimal_rounding():
    assert celsius_to_fahrenheit(36.6) == 97.88