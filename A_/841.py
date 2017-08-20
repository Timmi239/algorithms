from collections import defaultdict


def main():
    counts = input().split(' ')
    letters = input()
    _, k = map(int, counts)
    result = task(letters, k)
    print(result)


def task(letters: str, k: int):
    letters_dict = defaultdict(int)
    for letter in letters:
        letters_dict[letter] += 1

    if any(True for value in letters_dict.values() if value > k):
        return 'NO'
    else:
        return 'YES'


def test_1():
    assert task('aabb', 2) == 'YES'


def test_2():
    assert task('aacaab', 3) == 'NO'
