from typing import Any


def binary_search(
        target: Any,
        collection: list | tuple | str
) -> bool:
    """ Binary search algorithm implementation.

    :param target: Element to search for (no type-check in Python as collection
        can store multiple types).
    :param collection: An ordered & subscriptable container assumed to be already
        sorted in ascending order.
    :returns: False if collection is empty or element not present; otherwise, True.
    """

    low, high = 0, len(collection) - 1
    while low <= high:
        middle = (low + high) // 2
        if collection[middle] == target:
            return True
        elif collection[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return False
