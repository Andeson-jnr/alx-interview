#!/usr/bin/python3
"""
This module defines the function `canUnlockAll` that determines if all boxes
in a list of lists can be unlocked using the keys available in the boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.
    
    Args:
        boxes (list of lists): A list where each index represents a box and
                               each element is a list of keys found in that box.
    
    Returns:
        bool: True if all boxes can be unlocked, else False.
    """
    n = len(boxes)
    unlocked = set()
    unlocked.add(0)  # The first box is always unlocked
    stack = [0]  # To simulate unlocking process

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
