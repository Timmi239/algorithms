# Дано целое число 1≤n≤10^3 и массив A[1…n] натуральных чисел, не превосходящих 2⋅10^9.
# Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n длины k,
# в которой каждый элемент делится на предыдущий
# (формально: для  всех 1≤j<k, A[ij]|A[ij+1]).


def main():
    _ = int(input())
    num_list = list(map(int, input().split()))
    lis(num_list)


def lis(num_list):
    d = [-1] * len(num_list)
    for i in range(len(num_list)):
        d[i] = 1
        for j in range(i):
            if not num_list[i] % num_list[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = 0
    max_d = max(d)
    ans = max(max_d, ans)
    print(ans)


main()
