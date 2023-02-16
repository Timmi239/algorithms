from unittest import TestCase


def main() -> None:
    x_coordinates: list[int] = []
    y_coordinates: list[int] = []
    for _ in range(int(input())):
        x, y = input().split()
        x_coordinates.append(int(x))
        y_coordinates.append(int(y))
    x1, y1, x2, y2 = count_rectangle(x_coordinates, y_coordinates)
    print(f"{x1} {y1} {x2} {y2}")


def count_rectangle(x_coordinates: list[int], y_coordinates: list[int]) -> tuple[int, int, int, int]:
    return min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates)


if __name__ == "__main__":
    main()


class Tests(TestCase):
    def test_example(self):
        assert count_rectangle([1, 1, 5], [1, 10, 5]) == ((1, 1), (5, 10))
