from rpn import calc

def test_empty_string():
    assert calc("") == 0

def test_0_returns_0():
    assert calc("0") == 0

def test_2_returns_2():
    assert calc("2") == 2

def test_2_plus_2_returns_4():
    assert calc("2 2 +") == 4

def test_2_plus_2_plus_2_returns_6():
    assert calc("2 2 2 + +") == 6

def test_2_plus_3_plus_4_returns_9():
    assert calc("2 3 + 4 +") == 9

def test_3_times_4_returns_12():
    assert calc("3 4 *") == 12

def test_12_divided_by_4_returns_3():
    assert calc("12 4 /") == 3

def test_12_minus_4_returns_8():
    assert calc("12 4 -") == 8

def test_5_times_8_plus_7_times_3_returns_141():
    assert calc("3 5 8 * 7 + *") == 141
