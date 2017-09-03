def main():
    count = input()
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
