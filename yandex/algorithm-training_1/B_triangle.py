from itertools import permutations
from unittest import TestCase


def main():
    a, b, c = [int(input()) for _ in range(3)]
    if check_triangle(a, b, c):
        print("YES")
    else:
        print("NO")


def check_triangle(a: int, b: int, c: int) -> bool:
    return a < b + c and b < a + c and c < a + b


if __name__ == "__main__":
    main()


class TestStringMethods(TestCase):
    def test_1(self):
        for nums in permutations([3, 4, 5]):
            assert check_triangle(*nums)

    def test_zero(self):
        for nums in permutations([2, 1, 0]):
            assert not check_triangle(*nums)
