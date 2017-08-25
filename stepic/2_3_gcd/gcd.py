# найдите наибольший общий делитель


def gcd():
    inp = input().split()
    a, b = int(inp[0]), int(inp[1])
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(max(a, b))


gcd()
