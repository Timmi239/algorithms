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
    unique_numbers = set(first + second)

    pairs = 0
    for i in first:
        for j in second:
            if i ^ j in unique_numbers:
                pairs += 1

    return KOYOMI if pairs % 2 else KAREN


def test1():
    first = [1, 2, 3]
    second = [4, 5, 6]
    assert game(first, second) == KAREN


def test2():
    first = [2, 4, 6, 8, 10]
    second = [9, 7, 5, 3, 1]
    assert game(first, second) == KAREN
