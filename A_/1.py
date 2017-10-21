from math import ceil


def main():
    n, m, a = map(int, input().split())
    print(count_fields(n, m, a))


def count_fields(n, m, a):
    return ceil(n / a) * ceil(m / a)


def test1():
    assert count_fields(6, 6, 4) == 4


if __name__ == "__main__":
    main()
