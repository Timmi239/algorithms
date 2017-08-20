def main():
    inp1 = input().split(' ')
    _, sweets = map(int, inp1)
    inp2 = input().split(' ')
    sweets_counts = list(map(int, inp2))
    print(gift(sweets, sweets_counts))


def gift(sweets, sweets_counts):
    bran_total = 0
    aria_reserve = 0
    for i in range(len(sweets_counts)):
        current_day_sweets = aria_reserve + sweets_counts[i]
        to_bran = min(current_day_sweets, 8)
        bran_total += to_bran
        aria_reserve = current_day_sweets - to_bran

        if bran_total >= sweets:
            return i + 1

    return -1


def test_1():
    assert gift(3, [1, 2]) == 2


def test_2():
    assert gift(17, [10, 10, 10]) == 3


def test_3():
    assert gift(9, [10]) == -1
