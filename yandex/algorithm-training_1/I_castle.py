from itertools import combinations, permutations
from unittest import TestCase


def main():
    block_a, block_b, block_c, hole_d, hole_e = [int(input()) for _ in range(5)]
    if check_size(block_a, block_b, block_c, hole_d, hole_e):
        print("YES")
    else:
        print("NO")


def check_size(block_a: int, block_b: int, block_c: int, hole_d: int, hole_e: int) -> bool:
    for a, b in combinations([block_a, block_b, block_c], 2):
        for d, e in permutations([hole_d, hole_e], 2):
            if a <= d and b <= e:
                return True
    else:
        return False


if __name__ == "__main__":
    main()


class TestStringMethods(TestCase):
    def test_example_1(self):
        assert check_size(1, 1, 1, 1, 1)

    def test_example_2(self):
        assert not check_size(2, 2, 2, 1, 1)
