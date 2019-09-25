def change(amount):
    coins = []
    while amount > 0:
        coin = _get_coin(amount)
        amount -= coin
        coins.append(coin)
    return coins


def _get_coin(amount):
    for coin in (2, 1):
        if amount >= coin: return coin
