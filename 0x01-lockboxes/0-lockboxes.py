#!/usr/bin/python3
"""Check if all boxes (list of lists array where each element is a box
containing keys to other elements) are unlocked"""


def canUnlockAll(boxes):
    def explore(box_index, opened_boxes):
        opened_boxes.add(box_index)

        for key in boxes[box_index]:
            if key < len(boxes) and key not in opened_boxes:
                explore(key, opened_boxes)

    opened_boxes = set()
    explore(0, opened_boxes)

    return len(opened_boxes) == len(boxes)
