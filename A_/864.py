from collections import defaultdict


def main():
    count = int(input())
    number_to_count = defaultdict(int)
    for _ in range(count):
        number_to_count[int(input())] += 1

    is_win, cards = count_strategy(number_to_count)
    if is_win:
        print('YES')
        print('{} {}'.format(cards[0], cards[1]))
    else:
        print('NO')


def count_strategy(number_to_count):
    keys = list(number_to_count.keys())
    if len(keys) != 2:
        return False, []

    if number_to_count[keys[0]] == number_to_count[keys[1]]:
        return True, [keys[0], keys[1]]
    return False, []


def test1():
    result, numbers = count_strategy({11: 2, 27: 2})
    assert result
    assert sorted(numbers) == [11, 27]


def test2():
    result, numbers = count_strategy({2: 1, 6: 2})
    assert not result
    assert numbers == []


def test3():
    result, numbers = count_strategy({1: 2, 2: 2, 3: 3})
    assert not result
    assert numbers == []


if __name__ == "__main__":
    main()
