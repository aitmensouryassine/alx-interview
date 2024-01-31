#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    i = j = 0

    while i < len(data):
        bi = format(data[i], '08b')

        if bi.startswith("110"):
            j = 1
        elif bi.startswith("1110"):
            j = 2
        elif bi.startswith("11110"):
            j = 3
        else:
            i += 1

        while j:
            i += 1
            if i >= len(data):
                return False
            bi = format(data[i], '08b')
            if not bi.startswith('10'):
                return False
            j -= 1

    return True
