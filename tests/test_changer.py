from changer import changer


def test_returns_1_penny_when_passed_1():
    assert changer.change(1) == [1]


def test_returns_2p_when_passed_2():
    assert changer.change(2) == [2]



