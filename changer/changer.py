def change(amount):
    coins = []
    for coin in (200, 100, 50, 20, 10, 5, 2, 1):
        while amount >= coin:
            coins.append(coin)
            amount -= coin
    return coins
