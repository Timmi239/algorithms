def main():
    n = int(input())
    data = input().split(' ')
    rates = [int(i) for i in data]
    print(distribution(n, rates))


def distribution(count, rates):
    rates.sort(reverse=True)
    if rates[count - 1] > rates[count]:
        return 'YES'
    return 'NO'


def test_1():
    assert distribution(2, [1, 3, 2, 4]) == 'YES'


def test_2():
    assert distribution(1, [3, 3]) == 'NO'


def test_3():
    assert distribution(3, [3, 3, 3, 3, 4, 5]) == 'NO'
