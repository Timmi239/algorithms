def main():
    n = int(input())
    lines = [input() for i in range(n)]
    [print(l) for l in translator(lines)]


def translator(lines):
    translated_lines = []
    for l in lines:
        if is_rc_format(l):
            translated_lines.append(translate_from_rc(l))
        else:
            translated_lines.append(translate_to_rc(l))
    return translated_lines


def is_rc_format(line):
    if 'R' in line and 'C' in line and line.index('C') - line.index('R') > 1:
        return True
    return False


def translate_from_rc(line):
    row_number_str = ''.join((line[1:line.index('C')]))
    column_number_str = ''.join(line[(line.index('C') + 1):])
    column_number = int(column_number_str)

    result = ''

    while column_number > 0:
        if column_number % 26 == 0:
            result = 'Z' + result
            column_number = (column_number - 26) // 26
        else:
            result = chr((column_number % 26) + 64) + result
            column_number = column_number // 26

    return '{}{}'.format(result, row_number_str)

    # column_number_in_26 = int(column_number_str, 26)


def translate_to_rc(line):
    row_number_str = ''
    column_number = 0

    for ch in line:
        if ch.isdigit():
            row_number_str += ch
        else:
            column_number = column_number * 26 + (ord(ch) - 64)

    return 'R{}C{}'.format(row_number_str, column_number)


def test1():
    assert translator(['R23C55', 'BC23']) == ['BC23', 'R23C55']


def test2():
    assert translator(['AP55']) == ['R55C42']


def test3():
    assert translator(['R228C494']) == ['RZ228']


if __name__ == "__main__":
    main()
