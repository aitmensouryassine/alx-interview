#!/usr/bin/python3
"""Prime Number Game"""


def primes(n):
    """Returns a list of prime nums <= n"""
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return [n for n in range(2, n+1) if prime[n]]


def isWinner(x, nums):
    """Determines the winner"""

    # memoization
    allPrimes = primes(max(nums))

    score = 0
    for i in range(x):
        score = score + 1 if len([n for n in allPrimes if n <= nums[i]]) % 2 \
            else score - 1

    if score == 0:
        return None
    if score > 0:
        return 'Maria'
    return 'Ben'
