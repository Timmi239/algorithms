# Дано целое число 1≤n≤10^5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9.
# Найдите наибольшую невозрастающую подпоследовательность в A.
# В первой строке выведите её длину k, во второй — её индексы 1≤i1<i2<…<ik≤n
# (таким образом, A[i1]≥A[i2]≥…≥A[in]).


import bisect


def main():
    _ = int(input())
    num_list = list(map(int, input().split()))
    lis2(list(reversed(num_list)))


def lis2(num_list):
    index_list = [[-1, 1]] * len(num_list)
    endings_list = [num_list[0]]
    endings_indexes_list = [0]

    for i in range(1, len(num_list)):
        insert_index = bisect.bisect_right(endings_list, num_list[i])

        if insert_index == 0:
            index_list[i] = [-1, 1]
            endings_list[0] = num_list[i]
            endings_indexes_list[0] = i

        elif insert_index == len(endings_list):
            index_list[i] = [endings_indexes_list[-1], index_list[endings_indexes_list[-1]][1] + 1]
            endings_list.append(num_list[i])
            endings_indexes_list.append(i)

        else:
            index_list[i] = [
                endings_indexes_list[insert_index - 1],
                index_list[endings_indexes_list[insert_index - 1]][1] + 1
            ]
            endings_list[insert_index] = num_list[i]
            endings_indexes_list[insert_index] = i

    last_elem_in_max_sub = max(index_list, key=lambda x: x[1])
    print(last_elem_in_max_sub[1])

    res = []
    i = len(index_list) - 1
    while i >= 0:
        if index_list[i] == last_elem_in_max_sub:
            res.append(str(len(num_list) - i))
            i = last_elem_in_max_sub[0]
            last_elem_in_max_sub = index_list[last_elem_in_max_sub[0]]
        else:
            i -= 1
    print(' '.join(res))


main()
