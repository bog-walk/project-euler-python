def binary_search(target, collection):
    """
    Collection provided assumed to be pre-sorted in
    ascending order. An empty collection will automatically
    return False.
    """
    left, right = 0, len(collection) - 1
    while left <= right:
        middle = (left + right) // 2
        if collection[middle] == target:
            return True
        elif collection[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False
