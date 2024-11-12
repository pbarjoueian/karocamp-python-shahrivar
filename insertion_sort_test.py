# # insertion_sort_test.py
# from insertion_sort import insertion_sort

# assert insertion_sort([3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
# assert insertion_sort([1, 1, 1]) == [1, 1, 1]
# assert insertion_sort([]) == []


import pytest

# insertion_sort_test.py
from insertion_sort import insertion_sort


def test_insertion_sort():
    assert insertion_sort([3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([1, 1, 1]) == [1, 1, 1]
    assert insertion_sort([]) == []


def test_no_argument_raises():
    with pytest.raises(TypeError):
        insertion_sort()


class TestExceptions:
    def test_no_argument_raises(self):
        with pytest.raises(TypeError):
            insertion_sort()

    def test_different_types_raises(self):
        with pytest.raises(TypeError):
            insertion_sort(["a", 1])
