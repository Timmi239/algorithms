# необходимо найти последнюю цифру n-го числа Фибоначчи.


def main():
    f = int(input())
    a = [1, 1]
    while len(a)<f:
        a.append((a[-1] + a[-2]) % 10)
    print(a[f-1])


main()
