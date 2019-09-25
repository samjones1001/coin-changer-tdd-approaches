def change(amount):
    return [coin for coin in _get_coins(amount)]


def _get_coins(amount):
    for coin in (50, 20, 10, 5, 2, 1):
        while amount >= coin:
            amount -= coin
            yield coin
