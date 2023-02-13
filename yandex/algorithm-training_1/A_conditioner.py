from enum import Enum
from unittest import TestCase


class Mode(Enum):
    freeze = "freeze"
    heat = "heat"
    auto = "auto"
    fan = "fan"


def main() -> None:
    troom, tcond = [int(i) for i in input().split()]
    command = Mode(input())
    print(count_temperature(troom, tcond, command))


def count_temperature(troom: int, tcond: int, command: Mode) -> int:
    match command:
        case Mode.heat:
            return max(troom, tcond)
        case Mode.freeze:
            return min(troom, tcond)
        case Mode.fan:
            return troom
        case Mode.auto:
            return tcond


if __name__ == "__main__":
    main()


class TestStringMethods(TestCase):
    def test_heat_1(self):
        assert count_temperature(10, 20, Mode.heat) == 20

    def test_heat_2(self):
        assert count_temperature(20, 10, Mode.heat) == 20

    def test_freeze_1(self):
        assert count_temperature(10, 20, Mode.freeze) == 10

    def test_freeze_2(self):
        assert count_temperature(20, 10, Mode.freeze) == 10

    def test_fan_1(self):
        assert count_temperature(10, 20, Mode.fan) == 10

    def test_fan_2(self):
        assert count_temperature(20, 10, Mode.fan) == 20

    def test_auto_1(self):
        assert count_temperature(10, 20, Mode.auto) == 20

    def test_auto_2(self):
        assert count_temperature(20, 10, Mode.auto) == 10
