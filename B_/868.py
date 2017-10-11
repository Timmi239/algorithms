def main():
    string = input()
    if is_contest_in_time(*map(int, string.split())):
        print('YES')
    else:
        print('NO')


def is_contest_in_time(h, m, s, t1, t2):
    h = _hours_to_ticks(h, m, s)
    m = m + s / 60
    t1 = _hours_to_ticks(t1)
    t2 = _hours_to_ticks(t2)

    sorted_positions = sorted([h, m, s, t1, t2])
    current_position = sorted_positions.index(t1)
    contest_position = sorted_positions.index(t2)
    diff = abs(current_position - contest_position)
    return diff == 1 or diff == 4


def _hours_to_ticks(h, m=0, s=0):
    return h * 5 % 60 + m / 60 + s / 3600


def test1():
    assert not is_contest_in_time(12, 30, 45, 3, 11)


def test2():
    assert is_contest_in_time(12, 0, 1, 12, 1)


def test3():
    assert is_contest_in_time(3, 47, 0, 4, 9)


main()
