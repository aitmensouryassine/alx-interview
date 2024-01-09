#!/usr/bin/python3
"""Check if all boxes (list of lists array where each element is a box
containing keys to other elements) are unlocked"""


def canUnlockAll(boxes):
    """Check if all boxes are unlocked"""
    def unlock_boxes(boxes, keys, unlocked_boxes):

        if len(unlocked_boxes) == len(boxes):
            return True

        for key in keys:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)
                if unlock_boxes(boxes, boxes[key], unlocked_boxes):
                    return True
        return False

    unlocked_boxes = set()
    unlocked_boxes.add(0)
    return unlock_boxes(boxes, boxes[0], unlocked_boxes)
