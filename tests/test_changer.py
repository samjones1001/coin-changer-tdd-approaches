from changer import changer


def test_returns_1_penny_when_passed_1():
    assert changer.change(1) == [1]


def test_returns_2p_when_passed_2():
    assert changer.change(2) == [2]


def test_returns_2p_and_a_penny_when_passed_3():
    assert changer.change(3) == [2, 1]


def test_returns_5p_when_passed_5():
    assert changer.change(5) == [5]


