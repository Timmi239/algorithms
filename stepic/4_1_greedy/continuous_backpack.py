# Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6.
# Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6 и объём 0<wi≤2⋅10^6 предмета
# (n, W, ci, wi — целые числа).
# Выведите максимальную стоимость частей предметов
# (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
# помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.


def main():
    knapsack, objects_list = inp()
    sum_knapsack = 0
    objects_list.sort(key=lambda x: x[0]/x[1], reverse=True)
    for object_l in objects_list:
        if knapsack == 0:
            break
        if knapsack >= object_l[1]:
            sum_knapsack += object_l[0]
            knapsack -= object_l[1]
        else:
            sum_knapsack += object_l[0]*knapsack/object_l[1]
            break
    print(sum_knapsack)


def inp():
    count, knapsack = list(map(int, input().split()))
    objects_list = []
    for i in range(count):
        obj = input()
        objects_list.append(list(map(int, obj.split())))
    return knapsack, objects_list


main()
