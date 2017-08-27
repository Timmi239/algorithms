# По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
# постройте оптимальный беспрефиксный код.
# В первой строке выведите количество различных букв k, встречающихся в строке,
# и размер получившейся закодированной строки.
# В следующих k строках запишите коды букв в формате "letter: code".
# В последней строке выведите закодированную строку.

from heapq import *


def main():
    string = input()
    chars_set = set(string)
    chars_dict = dict()
    for char_i in string:
        if not chars_dict.get(char_i):
            chars_dict[char_i] = 1
        else:
            chars_dict[char_i] += 1
    chars_use = [(value, key) for key, value in chars_dict.items()]
    heapify(chars_use)
    new_chars_use = []
    while len(chars_use) > 1:
        smallest1 = heappop(chars_use)
        smallest2 = heappop(chars_use)
        heappush(chars_use, (smallest1[0] + smallest2[0], smallest1[1] + smallest2[1]))
        new_chars_use.append([smallest1[1],smallest2[1]])
    if not new_chars_use:
        print(str(len(chars_set)) + ' ' + str(len(string)))
        print(chars_use[0][1] + ': 0')
        print('0'*chars_use[0][0])
        return
    new_chars_dict = dict()
    for char_list in new_chars_use:
        for i in [0, 1]:
            for ch in char_list[i]:
                if not new_chars_dict.get(ch):
                    new_chars_dict[ch] = str(i)
                else:
                    new_chars_dict[ch] = str(i) + new_chars_dict[ch]
    coded = ''.join([new_chars_dict[s] for s in string])
    print(str(len(chars_set)) + ' ' + str(len(coded)))
    for key, value in new_chars_dict.items():
        print(key + ': ' + value)
    print(coded)


main()
