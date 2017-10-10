def main():
    input()
    print(more_from_seattle(input()))


def more_from_seattle(cities):
    from_seattle = 0
    from_san = 0

    current = cities[0]
    for c in cities[1:]:
        if current == c:
            continue
        if current == 'S':
            from_seattle += 1
        else:
            from_san += 1
        current = c

    if from_seattle > from_san:
        return 'YES'
    return 'NO'


def test1():
    assert more_from_seattle('FSSF') == 'NO'


def test2():
    assert more_from_seattle('SF') == 'YES'


def test3():
    assert more_from_seattle('FFFFFFFFFF') == 'NO'


def test4():
    assert more_from_seattle('SSFFSFFSFF') == 'YES'
