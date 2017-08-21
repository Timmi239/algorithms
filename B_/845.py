def main():
    data = input()
    ticket_numbers = list(map(int, data))
    print(prepare_ticket_parts(ticket_numbers))


def prepare_ticket_parts(numbers):
    first_part = numbers[:3]
    second_part = numbers[3:]
    if sum(first_part) > sum(second_part):
        return start_cheat(first_part, second_part)
    else:
        return start_cheat(second_part, first_part)


def start_cheat(big_part, small_part, changes=0):
    if sum(big_part) == sum(small_part):
        return changes

    changes += 1
    min_number = min(small_part)
    min_index = small_part.index(min_number)
    max_number = max(big_part)
    max_index = big_part.index(max_number)

    if 9 - min_number > max_number:
        if sum(big_part) - sum(small_part) > 9 - min_number:
            big_part[max_index] = 0
            return start_cheat(big_part, small_part, changes)
        return changes

    else:
        if sum(big_part) - sum(small_part) > max_number:
            small_part[min_index] = 9
            return start_cheat(big_part, small_part, changes)
        return changes


def test_1():
    assert prepare_ticket_parts([0, 0, 0, 0, 0, 0]) == 0


def test_2():
    assert prepare_ticket_parts(list(range(1, 7))) == 2


def test_3():
    assert prepare_ticket_parts([1, 1, 1, 0, 0, 0]) == 1


def test_4():
    assert prepare_ticket_parts([9, 9, 9, 0, 0, 0]) == 3


def test_5():
    assert prepare_ticket_parts([6, 6, 6, 8, 7, 7]) == 1
