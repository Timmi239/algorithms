def main():
    pwd = input()
    words_count = int(input())
    words = [input() for _ in range(words_count)]
    if is_password_hacked(pwd, words):
        print('YES')
    else:
        print('NO')


def is_password_hacked(pwd, words):
    if pwd in words:
        return True
    words_ends_with_first_letter_from_pwd = list(filter(lambda w: pwd[0] == w[1], words))
    words_starts_with_second_letter_from_pwd = list(filter(lambda w: pwd[1] == w[0], words))
    if words_ends_with_first_letter_from_pwd and words_starts_with_second_letter_from_pwd:
        return True
    return False


def test1():
    assert is_password_hacked('ya', ['ah', 'oy', 'to', 'ha'])


def test2():
    assert not is_password_hacked('hp', ['ht', 'tp'])


def test3():
    assert is_password_hacked('ah', ['ha'])
