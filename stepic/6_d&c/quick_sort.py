# В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно.
# Следующие n строк содержат по два целых числа ai и bi (ai≤bi) — координаты концов отрезков.
# Последняя строка содержит m целых чисел — координаты точек.
# Все координаты не превышают 10^8 по модулю.
# Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
# Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.


import bisect


def inp():
    counts = input()
    count_segments, count_point = map(int, counts.split())
    segments_list = []
    for i in range(count_segments):
        segments_list.append(list(map(int, input().split())))
    points = input()
    points_list = list(map(int, points.split()))
    return segments_list, points_list


def main():
    segments_list, points_list = inp()
    sorted_right_segments_list = sorted([segment[0] for segment in segments_list])
    sorted_left_segments_list = sorted([segment[1] for segment in segments_list])
    result = []
    for point in points_list:
        index_right = bisect.bisect_right(sorted_right_segments_list, point)
        index_left = bisect.bisect_left(sorted_left_segments_list, point)
        result.append(index_right - index_left)
    print(' '.join(map(str, result)))


main()
