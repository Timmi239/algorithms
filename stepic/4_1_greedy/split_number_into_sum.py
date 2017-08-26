# По данному числу 1≤n≤10^9 найдите максимальное число k,
# для которого n можно представить как сумму k различных натуральных слагаемых.
# Выведите в первой строке число k, во второй — k слагаемых.


def main():
    number = int(input())
    count = 0
    result = []
    for i in range(1, number // 2 + 2):
        if number - i > i:
            number -= i
            result.append(i)
            count += 1
        else:
            result.append(number)
            break
    print(len(result))
    print(' '.join(list(map(str, result))))


main()
