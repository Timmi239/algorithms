# Восстановите строку по её коду и беспрефиксному коду символов.
# В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв,
# встречающихся в строке, и размер получившейся закодированной строки, соответственно.
# В следующих k строках записаны коды букв в формате "letter: code".
# Ни один код не является префиксом другого.
# Буквы могут быть перечислены в любом порядке.
# В качестве букв могут встречаться лишь строчные буквы латинского алфавита;
# каждая из этих букв встречается в строке хотя бы один раз.
# Наконец, в последней строке записана закодированная строка.
# Исходная строка и коды всех букв непусты.
# Заданный код таков, что закодированная строка имеет минимальный возможный размер.
#
# В первой строке выходного файла выведите строку s.
# Она должна состоять из строчных букв латинского алфавита.
# Гарантируется, что длина правильного ответа не превосходит 10^4 символов.


def main():
    chars_dict = dict()
    count_chars, code_length = input().split()
    for i in range(int(count_chars)):
        char_inp = input().split()
        chars_dict[char_inp[0][:-1]] = char_inp[1]
    encode_string = input()
    result = ''
    sss = ''
    for i in range(len(encode_string)):
        sss += encode_string[i]
        for k, v in chars_dict.items():
            if v == sss:
                result += k
                sss = ''
    print(result)


main()
