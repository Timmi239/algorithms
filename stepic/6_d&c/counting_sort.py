# Первая строка содержит число 1≤n≤10^4, вторая — n натуральных чисел, не превышающих 10.
# Выведите упорядоченную по неубыванию последовательность этих чисел.


def main():
    _ = input()
    numbers_list = list(map(int, input().split()))
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in numbers_list:
        result[i - 1] += 1
    result_str = ''
    for i in range(10):
        if result[i] > 0:
            result_str += (str(i + 1) + ' ') * result[i]
    print(result_str)


main()
