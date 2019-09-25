def change(amount):
    return [coin for coin in _get_max_denomination(amount)]


def _get_max_denomination(amount):
    for coin in (10, 5, 2, 1):
        while amount >= coin:
            amount -= coin
            yield coin
