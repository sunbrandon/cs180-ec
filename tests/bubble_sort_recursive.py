from typing import Any, List

def bubble_sort_recursive(collection: List[Any]) -> List[Any]:
    """It is similar iterative bubble sort but recursive.

    :param collection: mutable ordered sequence of elements
    :return: the same list in ascending order

    """

    length = len(collection)
    swapped = False
    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            collection[i], collection[i + 1] = collection[i + 1],
    collection[i]
    swapped = True
    
    return collection if not swapped else bubble_sort_recursive(collection)