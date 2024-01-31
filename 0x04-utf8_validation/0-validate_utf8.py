#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    if len(data) == 1 and data[0] <= 127:
        return True
    return False
