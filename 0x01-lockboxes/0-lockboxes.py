#!/usr/bin/python3
"""Check if all boxes (list of lists array where each element is a box
containing keys to other elements) are unlocked"""


def canUnlockAll(boxes):
    """Check if all boxes are unlocked"""

    if not isinstance(boxes, list):
        return False

    if not all(isinstance(box, list) for box in boxes):
        return False

    if len(boxes) == 0:
        return False

    unlockedBoxes = [0]

    def unlockboxes(boxes, keys, unlockedboxes):
        for key in keys:
            if key in unlockedBoxes or key >= len(boxes):
                continue
            else:
                unlockedboxes.append(key)
                unlockboxes(boxes, boxes[key], unlockedboxes)

    unlockboxes(boxes, boxes[0], unlockedBoxes)

    if len(unlockedBoxes) == len(boxes):
        return True
    else:
        return False
