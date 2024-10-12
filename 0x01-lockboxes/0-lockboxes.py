#!/usr/bin/python3
"""
Module for the canUnlockAll function.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes (list of lists): A list of lists where each inner list represents a box
                           and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = set([0])  # The first box is already unlocked
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
