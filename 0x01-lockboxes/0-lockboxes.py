#!/usr/bin/python3
"""Check if all boxes (list of lists array where each element is a box
containing keys to other elements) are unlocked"""


def canUnlockAll(boxes):
    """Check if all boxes are unlocked"""

    unlockedBoxes = [0]

    def unlockboxes(boxes, keys, unlockedboxes):
        for key in keys:
            if key in unlockedBoxes:
                continue
            else:
                unlockedboxes.append(key)
                unlockboxes(boxes, boxes[key], unlockedboxes)

    unlockboxes(boxes, boxes[0], unlockedBoxes)

    if len(unlockedBoxes) == len(boxes):
        return True
    else:
        return False
