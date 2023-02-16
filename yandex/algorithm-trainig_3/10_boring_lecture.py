from collections import defaultdict
from unittest import TestCase


def main() -> None:
    word = input()
    letters_counts = count_letters(word)
    for letter, count in sorted(letters_counts.items()):
        print(f"{letter}: {count}")


def count_letters(word: str) -> dict[str, int]:
    result = defaultdict(int)
    word_len = len(word)
    for i in range(word_len):
        result[word[i]] += (word_len - i) * (i + 1)
    return result


if __name__ == "__main__":
    main()


class Tests(TestCase):
    def test_example_1(self):
        assert count_letters("hello") == {"e": 8, "h": 5, "l": 17, "o": 5}

    def test_example_2(self):
        assert count_letters("abacaba") == {"a": 44, "b": 24, "c": 16}
