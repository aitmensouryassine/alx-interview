#!/usr/bin/python3
"""Minimum Operations to print n times of a letter (H)"""

COPY_ALL_PASTE = "copy_all_paste"
PASTE = "paste"


def operation(op, oldNumH, numH, numOp, n):
    """It does two operations: copy all and paste or paste"""

    if op == COPY_ALL_PASTE:
        numOp += 2
        oldNumH = numH
        numH = numH * 2
        if numH > n:
            return -1
        elif numH == n:
            return numOp
        else:
            numOp1 = operation(COPY_ALL_PASTE, oldNumH, numH, numOp, n)
            numOp2 = operation(PASTE, oldNumH, numH, numOp, n)
            if numOp1 == -1 and numOp2 == -1:
                return -1
            elif numOp1 == -1:
                return numOp2
            elif numOp2 == -1:
                return numOp1
            else:
                return numOp1 if numOp1 < numOp2 else numOp2
    elif op == PASTE:
        numOp += 1
        numH = numH + oldNumH
        if numH > n:
            return -1
        elif numH == n:
            return numOp
        else:
            numOp1 = operation(COPY_ALL_PASTE, oldNumH, numH, numOp, n)
            numOp2 = operation(PASTE, oldNumH, numH, numOp, n)
            if numOp1 == -1 and numOp2 == -1:
                return -1
            elif numOp1 == -1:
                return numOp2
            elif numOp2 == -1:
                return numOp1
            else:
                return numOp1 if numOp1 < numOp2 else numOp2


def minOperations(n):
    """Returns the min num of operations to
    result exactly in n times H chars"""

    oldNumH = 1

    if type(n) is not int or n < 2:
        return 0

    numH = 2
    numOp = 2

    if n == numH:
        return numOp

    try:
        numOp1 = operation(COPY_ALL_PASTE, oldNumH, numH, numOp, n)
        numOp2 = operation(PASTE, oldNumH, numH, numOp, n)
    except Exception:
        return 0

    if numOp1 == -1 and numOp2 == -1:
        return 0
    elif numOp1 == -1:
        return numOp2
    elif numOp2 == -1:
        return numOp1
    else:
        return numOp1 if numOp1 < numOp2 else numOp2
