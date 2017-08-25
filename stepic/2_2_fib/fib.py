# вычислить n-е число Фибоначчи


def fib():
    f = int(input())
    a = [0, 1]
    while len(a) <= f:
        a.append(a[-1] + a[-2])
    print(a[f])


fib()
