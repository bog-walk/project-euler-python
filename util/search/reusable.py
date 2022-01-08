def binary_search(target, collection) -> bool:
    """
    :param target: Element to search for (no type-check
    in Python as collection can store multiple types).
    :param collection: Assumed to be already sorted
    in ascending order.
    :return: False if collection is empty or element not
    present; True otherwise.
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
