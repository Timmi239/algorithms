# По данным n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек.
#
# В первой строке дано число 1≤n≤100 отрезков.
# Каждая из последующих n строк содержит по два числа 0≤l≤r≤10^9, задающих начало и конец отрезка.
# Выведите оптимальное число m точек и сами m точек.
# Если таких множеств точек несколько, выведите любое из них.


def main():
    segment_list = inp()
    segment_list.sort(key=lambda x: x[1])
    result = recursion([], segment_list)
    print(len(result))
    print(' '.join(list(map(str, result))))


def recursion(result, segment_list):
    if segment_list:
        result.append(segment_list[0][1])
        new_segment_list = [segment for segment in segment_list if segment[0] > segment_list[0][1]]
        recursion(result, new_segment_list)
    return result


def inp():
    count = int(input())
    segment_list = []
    for i in range(count):
        segment_list.append(list(map(int, input().split())))
    return segment_list


main()
