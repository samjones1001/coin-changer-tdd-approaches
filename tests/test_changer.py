from changer import changer


def test_it_correctly_handles_sums_requiring_1_coin():
    assert changer.change(1) == [1]
    assert changer.change(2) == [2]
    assert changer.change(5) == [5]
    assert changer.change(10) == [10]


