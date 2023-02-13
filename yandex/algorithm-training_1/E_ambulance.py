import math
from itertools import product
from unittest import TestCase


INVALID_INPUT = (-1, -1)


def main() -> None:
    room_number_1, floors, room_number_2, entrance_2, floor_2 = [int(i) for i in input().split()]
    entrance_1, floor_1 = calculate_data(room_number_1, floors, room_number_2, entrance_2, floor_2)
    print(f"{entrance_1} {floor_1}")


def calculate_data(
    room_number_1: int, floors: int, room_number_2: int, entrance_2: int, floor_2: int
) -> tuple[int, int]:
    if floors < floor_2:
        return INVALID_INPUT

    if entrance_2 == 1 and floor_2 == 1:
        return try_to_guess_without_floors(room_number_1, room_number_2, floors)

    return find_possible_per_floor_numbers(room_number_1, room_number_2, entrance_2, floor_2, floors)


def try_to_guess_without_floors(room_number_1: int, room_number_2: int, floors: int) -> tuple[int, int]:
    if room_number_1 <= room_number_2:
        return (1, 1)

    floor = 1 if floors == 1 else 0
    entrance = 1 if room_number_1 <= (room_number_2 * floors) else 0
    return entrance, floor


def find_possible_per_floor_numbers(
    room_number_1: int, room_number_2: int, entrance_2: int, floor_2: int, floors: int
) -> tuple[int, int]:
    full_floors_before = (entrance_2 - 1) * floors + floor_2 - 1
    max_per_floor = (room_number_2 - 1) // full_floors_before
    min_per_floor = math.ceil(room_number_2 / (full_floors_before + 1))
    if min_per_floor > max_per_floor or max_per_floor == 0:
        return INVALID_INPUT

    min_entrance_1, min_floor_1 = count_result_by_possible_per_floor(room_number_1, min_per_floor, floors)
    max_entrance_1, max_floor_1 = count_result_by_possible_per_floor(room_number_1, max_per_floor, floors)
    entrance_1 = min_entrance_1 + 1 if min_entrance_1 == max_entrance_1 else 0
    floor_1 = min_floor_1 + 1 if min_floor_1 == max_floor_1 or floors == 1 else 0
    return entrance_1, floor_1


def count_result_by_possible_per_floor(room_number: int, per_floor: int, floors: int) -> tuple[int, int]:
    floors_1 = (room_number - 1) // per_floor
    return floors_1 // floors, floors_1 % floors


if __name__ == "__main__":
    main()


class TestStringMethods(TestCase):
    def test_example(self):
        assert calculate_data(89, 20, 41, 1, 11) == (2, 3)
        assert calculate_data(90, 20, 41, 1, 11) == (2, 3)
        assert calculate_data(91, 20, 41, 1, 11) == (2, 3)
        assert calculate_data(92, 20, 41, 1, 11) == (2, 3)

    def test_normal(self):
        for room_1, room_2 in product(range(31, 34), range(13, 16)):
            assert calculate_data(room_1, 3, room_2, 2, 2) == (4, 2)

    def test_normal_2(self):
        for room_1, room_2 in product(range(33, 37), range(17, 21)):
            assert calculate_data(room_1, 4, room_2, 2, 1) == (3, 1)

    def test_without_floor_and_entrance(self):
        assert calculate_data(530, 5, 10, 1, 1) == (0, 0)

    def test_only_floor_1(self):
        assert calculate_data(11, 1, 1, 1, 1) == (0, 1)

    def test_only_floor_2(self):
        assert calculate_data(59, 1, 30, 1, 1) == (0, 1)

    def test_only_entrance(self):
        assert calculate_data(3, 10, 1, 1, 1) == (1, 0)

    def test_only_entrance_2(self):
        assert calculate_data(40, 5, 30, 1, 2) == (1, 0)

    def test_only_entrance_3(self):
        assert calculate_data(59, 2, 30, 1, 2) == (2, 0)

    def test_only_entrance_4(self):
        assert calculate_data(100, 5, 30, 1, 1) == (1, 0)

    def test_3(self):
        assert calculate_data(3, 2, 2, 2, 1) == (-1, -1)

    def test_4(self):
        for i in range(1, 16):
            assert calculate_data(i, 5, 30, 1, 2) == (1, 1)

    def test_invalid_1(self):
        assert calculate_data(3, 2, 2, 2, 1) == INVALID_INPUT

    def test_invalid_2(self):
        assert calculate_data(15, 5, 2, 1, 3) == INVALID_INPUT
