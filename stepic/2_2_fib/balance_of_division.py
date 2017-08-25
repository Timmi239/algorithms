# необходимо найти остаток от деления n-го числа Фибоначчи на m.


def fib():
    f = input().split()
    n, m = int(f[0]), int(f[1])
    a = [0, 1, 1]
    while a[-1] != 1 or a[-2] != 0:
        a.append((a[-1] + a[-2]) % m)
    circle = len(a) - 2
    print(a[n % circle] % m)


fib()
