from typing import List


class Member:
    def __init__(self, parts, a_happy, b_happy):
        self.parts = parts
        self.a_happy = a_happy
        self.b_happy = b_happy

    @property
    def happy_diff(self):
        return self.a_happy - self.b_happy

    def __repr__(self):
        return '{} {} {}'.format(self.parts, self.a_happy, self.b_happy)


def main():
    input_strings_members, parts = read_input()
    members = prepare_members(input_strings_members)
    print(count_parts(members, parts))


def read_input():
    counts_str = input().split()
    members_count, parts = map(int, counts_str)
    return [input() for _ in range(members_count)], parts


def prepare_members(input_strings_members):
    return [Member(*map(int, line.split())) for line in input_strings_members]


def count_parts(members: List[Member], parts_in_one):
    a_members = list(filter(lambda m: m.happy_diff > 0, members))
    a_members.sort(key=lambda m: m.happy_diff, reverse=False)
    a_modulo = sum(m.parts for m in a_members) % parts_in_one

    a_modulo_members, a_happy_members = split_members_into_happy_groups(a_members, a_modulo)
    a_happy = sum(m.a_happy * m.parts for m in a_happy_members)

    b_members = list(filter(lambda m: m.happy_diff < 0, members))
    b_members.sort(key=lambda m: m.happy_diff, reverse=True)
    b_modulo = sum(m.parts for m in b_members) % parts_in_one

    b_modulo_members, b_happy_members = split_members_into_happy_groups(b_members, b_modulo)
    b_happy = sum(m.b_happy * m.parts for m in b_happy_members)

    other_members = list(filter(lambda m: m.happy_diff == 0, members))

    last_happy = count_last_pizzas_happy(a_modulo_members, b_modulo_members, other_members, parts_in_one)

    print(a_happy, b_happy, last_happy)
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

    print(modulo_members)
    print(happy_members)
    return modulo_members, happy_members


def count_last_pizzas_happy(a, b, other, parts_in_one):
    parts_count = sum(m.parts for m in a + b + other)
    if parts_count <= parts_in_one:
        a_happy = sum(m.a_happy * m.parts for m in a + b + other)
        b_happy = sum(m.b_happy * m.parts for m in a + b + other)
        return max(a_happy, b_happy)

    full_a_pizza_happy = 0
    full_b_pizza_happy = 0
    return max(full_a_pizza_happy, full_b_pizza_happy)


def test1():
    members = prepare_members(['7 4 7', '5 8 8', '12 5 8', '6 11 6', '3 3 7', '5 9 6'])
    assert count_parts(members, 10) == 314


def test2():
    members = prepare_members(['3 5 7', '4 6 7', '5 9 5'])
    assert count_parts(members, 12) == 84
