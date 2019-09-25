from changer import changer


def test_it_correctly_handles_sums_requiring_1_coin():
    assert changer.change(1) == [1]
    assert changer.change(2) == [2]
    assert changer.change(5) == [5]
    assert changer.change(10) == [10]


def test_it_correctly_handles_sums_requiring_2_coins():
    assert changer.change(3) == [2, 1]
    assert changer.change(6) == [5, 1]
    assert changer.change(7) == [5, 2]
    assert changer.change(11) == [10, 1]


def test_it_correctly_handles_sums_requiring_3_coins():
    assert changer.change(9) == [5, 2, 2]
    assert changer.change(13) == [10, 2, 1]
    assert changer.change(23) == [20, 2, 1]


def test_it_correctly_handles_sums_requiring_many_coins():
    assert changer.change(73) == [50, 20, 2, 1]
    assert changer.change(237) == [200, 20, 10, 5, 2]
    assert changer.change(349) == [200, 100, 20, 20, 5, 2, 2]
