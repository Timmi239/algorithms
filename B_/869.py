def main():
    inp = input().split()
    a, b = list(map(int, inp))
    print(div_factor(b, a))


def div_factor(b, a):
    last_digit = 1
    for i in range(a + 1, b + 1):
        last_digit = last_digit * i % 10
        if last_digit == 0:
            return last_digit
    return last_digit


def test1():
    assert div_factor(4, 2) == 2


def test2():
    assert div_factor(10, 0) == 0


def test3():
    assert div_factor(109, 107) == 2
