KOYOMI = 'Koyomi'
KAREN = 'Karen'


def main():
    input()
    first_str = input().split()
    first = list(map(int, first_str))
    second_str = input().split()
    second = list(map(int, second_str))
    print(game(first, second))


def game(first, second):
    numbers_dict = {}
    for lst in [first, second]:
        for i in lst:
            numbers_dict[i] = 0

    for i in first:
        for j in second:
            result = i ^ j
            if numbers_dict.get(result) is not None:
                numbers_dict[result] += 1

    return KOYOMI if sum(numbers_dict.values()) % 2 else KAREN


def test1():
    first = [1, 2, 3]
    second = [4, 5, 6]
    assert game(first, second) == KAREN


def test2():
    first = [2, 4, 6, 8, 10]
    second = [9, 7, 5, 3, 1]
    assert game(first, second) == KAREN
