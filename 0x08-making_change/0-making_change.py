#!/usr/bin/python3
"""Coin Change Problem"""


def makeChange(coins, total):
    """Coin change
    coins: list of available coins
    total: the amount"""

    if total <= 0:
        return 0

    coins.sort()
    ans = []
    i = len(coins) - 1

    while i >= 0:
        while total >= coins[i]:
            total = total - coins[i]
            ans.append(coins[i])
        i -= 1

    if len(ans) and total == 0:
        return len(ans)

    return -1
