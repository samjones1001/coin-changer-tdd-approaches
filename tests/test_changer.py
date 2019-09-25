from changer import changer


def test_returns_1_penny_when_passed_1():
    assert changer.change(1) == [1]


def test_returns_2p_when_passed_2():
    assert changer.change(2) == [2]


def test_returns_2p_and_a_penny_when_passed_3():
    assert changer.change(3) == [2, 1]


def test_returns_5p_when_passed_5():
    assert changer.change(5) == [5]


def test_returns_10p_when_passed_10():
    assert changer.change(10) == [10]


def test_returns_20p_when_passed_20():
    assert changer.change(20) == [20]


def test_returns_50p_when_passed_50():
    assert changer.change(50) == [50]


def test_returns_1_pound_when_passed_100():
    assert changer.change(100) == [100]


def test_returns_2_pounds_when_passed_200():
    assert changer.change(200) == [200]