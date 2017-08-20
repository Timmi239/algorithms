from typing import List, Optional

import pytest

Index = int


class NotFoundException(Exception):
    pass


def binary_search(a: List[int], el: int):
    return _binary_search(a, el, 0, len(a) - 1)


def _binary_search(a: List[int], el: int, left: Index = 0, right: Optional[Index] = None) -> Index:
    if left == right:
        if a[left] != el:
            raise NotFoundException()
        return left
    elif left > right:
        raise NotFoundException()

    mid = (left + right) // 2
    if a[mid] < el:
        left = mid + 1
    else:
        right = mid
    return _binary_search(a, el, left, right)


def test_empty():
    with pytest.raises(NotFoundException):
        assert binary_search([], 5)


def test_not_found():
    with pytest.raises(NotFoundException):
        assert binary_search([0, 1, 3, 4], 2)


def test_even_len():
    assert binary_search([0, 1, 2, 3, 4, 5], 2) == 2


def test_odd_len():
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 5) == 5


def test_right_border():
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 6) == 6


def test_left_border():
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 0) == 0
