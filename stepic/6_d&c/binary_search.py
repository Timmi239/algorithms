# В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел,
# не превышающих 10^9, в порядке возрастания,
# во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих 10^9.
# Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n,
# для которого A[j]=bi, или −1, если такого j нет.


def main():
    list_1, list_2 = inp()
    result = []
    for i in range(len(list_2)):
        result.append(binary_search(0, len(list_1) - 1, list_1, list_2[i]))
    print(' '.join(map(str, result)))


def binary_search(left, right, list_1, current_element):
    while left <= right:
        m = (left + right) // 2
        if list_1[m] < current_element:
            left = m + 1
        elif list_1[m] == current_element:
            return m + 1
        else:
            right = m - 1
    return -1


def inp():
    inp1, inp2 = input(), input()
    list_1 = list(map(int, inp1.split()[1:]))
    list_2 = list(map(int, inp2.split()[1:]))
    return list_1, list_2


main()
