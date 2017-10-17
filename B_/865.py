from collections import namedtuple


Member = namedtuple('Member', ['parts', 'a_happy', 'b_happy'])


def happy_diff(m):
    return m.a_happy - m.b_happy


def main():
    input_strings_members, parts = read_input()
    a_members, b_members, other_members = prepare_members(input_strings_members)
    print(count_parts(a_members, b_members, other_members, parts))


def read_input():
    counts_str = input().split()
    members_count, parts = map(int, counts_str)
    return [input() for _ in range(members_count)], parts


def prepare_members(input_strings_members):
    a_members = []
    b_members = []
    other_members = []
    for line in input_strings_members:
        m = Member(*map(int, line.split()))
        if happy_diff(m) > 0:
            a_members.append(m)
        elif happy_diff(m) < 0:
            b_members.append(m)
        else:
            other_members.append(m)
    return a_members, b_members, other_members


def count_parts(a_members, b_members, other_members, parts_in_one):
    a_members.sort(key=lambda m: happy_diff(m), reverse=False)
    a_modulo = sum(m.parts for m in a_members) % parts_in_one

    a_modulo_members, a_happy_members = split_members_into_happy_groups(a_members, a_modulo)
    a_happy = sum(m.a_happy * m.parts for m in a_happy_members)

    b_members.sort(key=lambda m: happy_diff(m), reverse=True)
    b_modulo = sum(m.parts for m in b_members) % parts_in_one

    b_modulo_members, b_happy_members = split_members_into_happy_groups(b_members, b_modulo)
    b_happy = sum(m.b_happy * m.parts for m in b_happy_members)

    last_happy = count_last_pizzas_happy(a_modulo_members, b_modulo_members, other_members, parts_in_one)

    return a_happy + b_happy + last_happy


def split_members_into_happy_groups(members, modulo):
    modulo_members = []
    happy_members = []
    current_modulo = 0

    for i in range(len(members)):
        m = members[i]
        if m.parts + current_modulo <= modulo:
            current_modulo += m.parts
            modulo_members.append(m)
        else:
            remaining_for_modulo_parts = modulo - current_modulo
            if remaining_for_modulo_parts > 0:
                modulo_members.append(Member(remaining_for_modulo_parts, m.a_happy, m.b_happy))
            happy_members.append(Member(m.parts - remaining_for_modulo_parts, m.a_happy, m.b_happy))
            if i < len(members) - 1:
                happy_members.extend(members[i+1:])
            break

    return modulo_members, happy_members


def count_last_pizzas_happy(a, b, other, parts_in_one):
    last_sorted_members = a + other + b

    current_parts = 0
    possible_a_members_happy = 0
    other_b_members_happy = 0
    for i in range(len(last_sorted_members)):
        m = last_sorted_members[i]
        new_current_parts = current_parts + m.parts
        if new_current_parts < parts_in_one:
            possible_a_members_happy += m.parts * m.a_happy
            current_parts = new_current_parts
            continue

        possible_a_members_happy += (parts_in_one - current_parts) * m.a_happy
        if new_current_parts > parts_in_one:
            other_b_members_happy = (new_current_parts - parts_in_one) * m.b_happy
        if i + i < len(last_sorted_members):
            other_b_members_happy += sum(m.parts * m.b_happy for m in last_sorted_members[(i + 1):])
        break

    current_parts = 0
    possible_b_members_happy = 0
    other_a_members_happy = 0
    for i in reversed(range(len(last_sorted_members))):
        m = last_sorted_members[i]
        new_current_parts = current_parts + m.parts
        if new_current_parts < parts_in_one:
            possible_b_members_happy += m.parts * m.b_happy
            current_parts = new_current_parts
            continue

        possible_b_members_happy += (parts_in_one - current_parts) * m.b_happy
        if new_current_parts > parts_in_one:
            other_a_members_happy = (new_current_parts - parts_in_one) * m.a_happy
        if i + i < len(last_sorted_members):
            other_a_members_happy += sum(m.parts * m.a_happy for m in last_sorted_members[:i])
        break

    return max(possible_a_members_happy + other_b_members_happy, possible_b_members_happy + other_a_members_happy)


def test1():
    a, b, c = prepare_members(['7 4 7', '5 8 8', '12 5 8', '6 11 6', '3 3 7', '5 9 6'])
    assert count_parts(a, b, c, 10) == 314


def test2():
    a, b, c = prepare_members(['3 5 7', '4 6 7', '5 9 5'])
    assert count_parts(a, b, c, 12) == 84


def test3():
    a, b, c = prepare_members(['2 3 1', '2 2 2', '2 1 3'])
    assert count_parts(a, b, c, 3) == 16


def test4():
    a, b, c = prepare_members(
        [
            '20000 3 1',
            '20000 2 2',
            '20000 1 3',
            '20000 3 1',
            '20000 2 2',
            '20000 1 3',
            '20000 3 1',
            '20000 2 2',
            '20000 1 3'
        ]
    )
    assert count_parts(a, b, c, 30000)


main()
