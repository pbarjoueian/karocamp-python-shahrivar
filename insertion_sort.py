# insertion_sort.py
def insertion_sort(unsorted):
    """Return a sorted version of a list."""
    sorted = []
    for new_item in unsorted:
        i = 0
        for sorted_item in sorted:
            if new_item >= sorted_item:
                i += 1
            else:
                break
        sorted.insert(i, new_item)
    return sorted


class A:
    pass


a = A()

insertion_sort([a, 1])
