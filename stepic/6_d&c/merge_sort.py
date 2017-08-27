# Первая строка содержит число 1≤n≤10^5, вторая — массив A[1…n], содержащий натуральные числа,
# не превосходящие 10^9.
# Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].

# (Такая пара элементов называется инверсией массива.
# Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
# например, в упорядоченном по неубыванию массиве инверсий нет вообще,
# а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)


def main():
    list_num = inp()
    print(count_inversion(list_num))


def count_inversion(sequence):
    def count(first, last):
        if last - first < 2:
            return 0
        middle = (first+last) // 2
        inversions = count(first, middle) + count(middle, last)
        i, j = first, middle
        ordered = []
        while i < middle and j < last:
            if sequence[i] <= sequence[j]:
                ordered.append(sequence[i])
                i += 1
            else:
                ordered.append(sequence[j])
                j += 1
                inversions += middle - i
        ordered.extend(sequence[i:middle])
        ordered.extend(sequence[j:last])
        sequence[first:last] = ordered
        return inversions
    return count(0, len(sequence))


def inp():
    _, list_num = input(), list(map(int, input().split()))
    return list_num


main()
