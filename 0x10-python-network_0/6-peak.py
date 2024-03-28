#!/usr/bin/python3
"""
Finds a peak in the given list of unsorted intgers
"""


def find_peak(list_of_integers):
    """
    Finds peak using binary approach
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
