"""import datetime
with open('a2.txt') as f:
    for i in f.readlines():
        li = [j.strip() for j in i.split()]
        d1 = datetime.datetime.strptime(li[0], "%d.%m.%Y")
        d2 = datetime.datetime.strptime(li[1], "%d.%m.%Y")
        delta = d1 - d2
        print(abs(delta.days))"""
# 2
# import itertools
# from random import shuffle
#
# def g():
#     abc = '0123456789abcdef'
#     res = []
#     for i1 in range(16):
#         for i2 in range(i1 + 1, 16):
#             for i3 in range(i2 + 1, 16):
#                 for i4 in range(i3 + 1, 16):
#                     for i5 in range(i4 + 1, 16):
#                         for i6 in range(i5 + 1, 16):
#                             s = set(abc[i1] + abc[i2] + abc[i3] + abc[i4] + abc[i5] + abc[i6])
#                             for el in res:
#                                 if len(s & el) > 4:
#                                     break
#                             else:
#                                 res.append(s)
#                             if len(res) > 100:
#                                 return(res)
#
# p = g()
# for i in range(len(p)):
#     for j in range(i + 1, len(p)):
#         if len(p[i] & p[j]) > 4:
#             print('!')
#             break
#     else:
#         print('OK')
# cnt = 0
# f = open('out70000.txt', 'w')
# r = []
# for el in p:
#     first = itertools.permutations(el)
#     for k in [''.join(x) for x in first]:
#         r.append(k)
#     shuffle(r)
# for k in r[:70000]:
#     print(k, file=f)
# f.close()

# 3
# with open('mos.d.txt') as f:
#     li = f.readlines()
#     t = int(li.pop(0))
#     for i in li:
#         if len(list(map(int, i.strip().split()))) == 3:
#             n, m, k = list(map(int, i.strip().split()))
#             smezh = {}
#             cnt = 1
#         else:
#             s, f = list(map(int, i.strip().split()))
#             if s not in smezh.keys():
#                 smezh[s] = [f]
#             else:
#                 smezh[s].append(f)
#             if not f in smezh.keys():
#                 smezh[f] = [s]
#             else:
#                 smezh[f].append(s)
#         li1 = {}
#         cnt = 1
#         print('smezh')
#         print(smezh)
#         for key, item in smezh.items():
#             #print(item)
#             for j in range(len(item)):
#                 if cnt not in li1.keys():
#                     li1[cnt] = [sorted([key, item[j]])]
#                 else:
#                     for z in li1[cnt]:
#                         if key in z or item[j] in z:
#                             continue
#                         if sorted([key, item[j]]) not in li1[cnt]:
#                             li1[cnt].append(sorted([key, item[j]]))
#                 if cnt <= k:
#                     cnt += 1
#                 else:
#                     cnt -= 1
#
#         print(li1)
#


#5
# di = {'l': '00', 'h': '01', 'e': '10', 'o': '11'}
# s = 'hello'
# res = ''
# for i in s:
#     res += di[i]
# binary = '1011000111'
# print(res, binary)

# print(binary == res)
from collections import Counter


sequence = "ieeccafjidaccjajfhejdegdbafcahhjjjijgifgdjfccgdbejicdbbidhiifiaaeiadfehffbgeegecijjcacfacgchgghdcifeebbaibfaajgabdchgbdjhibfjjajidgehjcbhdeefdjfbghhefbbcfhdgbbcaccdaijifejicfgabigaigccdbihfhjihbdeaeghbafhbbhadgafbhaebcbibjhgdejjdgcbfjddffdchegcajijhegbcjchgifihibdedcbecchdaajjdadaffieihhfagechicecieeehigbchfhhdhfcgjgjbfcajgeifijdihcdbdjcfgcdddfdgdaibdahgaffgjigejhbfheeeabhcdhhfjjbhhbigeidiheejfihaabecfebjhfcffihfdehdcgfaafcgceaabbibccgchfddgcbcgijjfgecgajbgbgcacfbacbdbccbchdjggeigjchjhdhhgefcaiccegfgfhhjegjiiabajbidjjcbegbeeaejdbhhdeeigjghcaedfdhbhjhbjcdhdfaffegihgigeeadahijaicbfccddejeacjcddfjaceihacabhhfjgidadidiijefacfdfjceaiceieebjgidjjciffiehfgeacafjgdfefcdedfecihgegfhjefchdebgaccaebaecjaaiegjgagcjdhbfejjjggdgibgiafieaabaaedghfbdjifcbdiecdjdfebbcbbihhhebjbcjjidceccaaebgffedhbejigihgdgbiaighcbaibbjgbfebajjicebjbfehhgfgcibejgagfgbdjghfabeahjgfcbicffceiighhggeidhgaejjacjcbaaedgebdagjccficeajjacgccgbhgfdhaiadeccfgcfbgcbjffddciejhiebeejhgcbbgbehfaadfdhdhafejbjhiibfaahghdhjfbccjcciedhaa"
encoded_sequence = "00000000100001000010010011000001000000000100000000100011001001000000000110000000001000001000000010000100000000010001000010000001000101100000100110000000100000001000000000100000000010000000001000000001000000000100000010000000010000010000001000100000000010000010010010000001000101000010000000001000000001001000101010000000010001000000010000000010000000010000010000000011100001000000001100010000010000100000001000001000001010000001000010000100000010000100100000000100000000010000000001001100100000110010000001001000000010000001000000100000001000100100000000100000100001000010101100000000101000001110000000001000000110100010010000000100000010100010000000001000000010000000010100000100000000010000000001100000000010000000010001000000100001000000010000000001001010000000100010000100001000001000100000000010000010100000010000000100000001000010000010101001000001000000010001000000101010011001001000110000000010000000001000000001000001000010000000001000000001001000001000000110100000000100000011000000001000000100100100010100000000100000001000001000000010000000001000000001000000010100010000110000100000010000000101100000100000001010100000001100010000001100000101000000011000010100101000000001010000000001000000010000001000100001000000000100000000010001000000100101000001000000000100010001000001000001000100100000001000010000001001100000000010000000010000000001000000010000100000010100100000000010010000000100000010000000010000010000000010000000100000000101000100001000100101000010010010000000100011100000000010000000001000110001100000100000100000000100001000000001000000010000000100000110000001000010010000000100000000100100001001000000001000010000100001000000010000000010000001010010000000100000100000001000000010001000000010000010010000001000000000100000010000000001010000010011000000000100000010000100000000100000100000000100000000010001000000001000000010010001010001000000000100100000100000010010001000100010000010001000000100011000000001010001100000001000000110000010000010000001000000000100000000100000010000100000000010000000101000001000000010000100001000011010000000100100010000000100000001000001000000000100000000010100000001000000010100000000100000010000100000000100010000000010000000100001000010000000001000001000000001000000011101000010010000010000101000000000100000001000001001000001000001000000001000000010000010001000010000000100010010000001000001110000010010000001001000011101010000000010100100100000010010000000100000100010001000000100101001000000100000000100000000010000000001000001000000100001001000000110000000001010000001010000001001100100000101100101000101001001010010000000100010000000001000000100000010000100000000100000010000000001001000000010000000001000000010001000000010000000100000010000100000100110000000010010010000100000010000010000001000001000000010000000100000000010000100000010000000001000000001000000001101100000000010100000000100010000000001000000000100101000010000001010000100001100001000000000100010100000001000000010001000010000100000000100000010000000001000000100000001001100001000100000100010000000101000000010000000001000000010100000000010010001000000010001000001100000100000100001000000100000000100000001000000100000000100000010000100001100011000000010000000010000000001100000000100101000001001001000100010000100000000010000110010000000001001000100010000010000000001100100001000000001000000011001101000000010000000100000100000000010000001000000001000110001000000001000100000000100000000100000000010000100000110010000010001000001000000000100100001100000000100100001000000001000010000101000000000100000010000000010001000000000100000000010010000000010000010000010000000010000100000001000001000000100001100110000010000000001000000100010000010000100000100100010000100010000010000100100000000100000001000000100001000000100000100000001000000000100001000001001000000010001000010100000011001001100001011000010010000000001110000000010000100000010000000001000000110000001001000000000100010000000101000001000010000000001000000000100000000010000001000000100010000001000000001010000001000000001100000100000000100001110111000010001000000100000001000001010001000000000100000000100000100101000100000000100001001000100000000010001000001000010101001010100000000100000001000000010000000100001010000000001010010000000001000000000100000000100010010000100100111000010100000010000010000010000100010000000101000010000000001000000001000000100000000100000001000000100010000001010000000011000000001000000100000001001011000000001010100000000010000001010000010000101100000000010000000001000000001001000010100000000010100000100001000000010000000100000010000010000001001000000001010000100000000010000001100000010000010000001010001000000000100000010000000100000110100001100000001000000000100000010000010010100000000100100000100000100100001000000001000000001000000100000001000000010000001000000100001000000001000100000001000000110000100000000010000000001100100000000010010111000010001000000100001010001100000010000000001001001000001000000001001000011000000000100000000011001000000100100100000010100000001000000100000100010000000110000000011000100001001001000001000000100100000101000000100101000000000100000100000100010001001000000001000010000000001000000010000000010000101000010000100000000010000000100000010010101000000101000010000000100000111000100000100010000000100010000000110000010000100000000010100000000010000000100000000100000000101000001110000000100000010000000100010000000100000000010000010100100100000000010010010000000010000100010000000111"
di = {'a': '1'}
# flag = False
freq = {}
for i in sequence:
    freq[i] = sequence.count(i)
# print(freq)
# cnt = 1
# while not flag:
#     for i in range(cnt, len(encoded_sequence)):
#         if encoded_sequence[i - cnt:i][0] == '1':
#             break
#         k = encoded_sequence.count(encoded_sequence[i - cnt:i])
#         if k in freq.values():
#             for j in freq.items():
#                 if k == j[1]:
#                     if j[0] != 'a':
#                         di[j[0]] = encoded_sequence[i - cnt:i]
#     print(di)
#     for i in di.items():
#         if not i[1]:
#             flag = False
#             di = {'a': '1'}
#     cnt += 1
# print(di)
# def func(letter):
#     cnt = 2
#     li2 = []
#     while cnt < 30:
#         if encoded_sequence.count(encoded_sequence[0:cnt]) >= freq[letter]:
#             li2.append(encoded_sequence[0:cnt])
#         cnt += 1
#     return li2
#
#
# # ищем i
# print(freq['i'])
# print('i * 2')
# li1 = []
# li = func('i')
# for i in li:
#     if encoded_sequence.count(i + i) >= 5:
#         li1.append(i)
# print(li[::-1])
# print('sequence')
# # i = 000000001000
# i = '000000001'
# encoded_sequence = (encoded_sequence[len('000000001'):])
# print('sequence after i')
# print(encoded_sequence)
# print('e', func('e'))
# # e = 00001
# e = '00001'
# encoded_sequence = encoded_sequence[len('00001') * 2:]
# print(encoded_sequence)
# # c = 001
# print('c', func('c'))
# c = '001'
# encoded_sequence = encoded_sequence[len('001') * 2 + 1:]
# print('encoded after ieecca')
# print(encoded_sequence)
# print('f', func('f'))
# # let f = 0000010000
# f = '000001'
# # f+g = 0000010000000001
# encoded_sequence = encoded_sequence[len('0000010'):]
# print(encoded_sequence)
# print('j', func('j'))
# #let j = 000001
# j = '0000000001'
# encoded_sequence = encoded_sequence[len('000001') + len('000000001'):]
# print(encoded_sequence)
# # let d = '0001'
# d = '0001'
# encoded_sequence = encoded_sequence[len('0001') + 1 + 2 * len(c) + len(j) + 1 + len(j) + len(f):]
# # теперь строка начинается с: hejd
# print(e, j, d)
# print(encoded_sequence)
# a = '1'
# s = (i+e+e+c+c+a+f+j+i+d+a+c+c+j+a+j + f)
# print(d, i)
# print('h', func("h"))
# h = '00100000001'
# print(i+e+e+c+c+a+f+j+i+d+a+c+c+j+a+j + f + h + e + j + d + e)
# + g + b + a + f)
#let d = 00010001100100100000000011000000000
# encoded_sequence = encoded_sequence[len('00010001100100100000000011000000000') + len('1000001'):]
# encoded_sequence = encoded_sequence[]
# sequence = "hello"
# encoded_sequence = "1011000111"
# print(fano_coding(sequence))


def F(n):
    if n == 0:
        return 0
    if n % 2:
        return 1 + F(n - 1)
    return F(n / 2)

cnt = 0
for i in range(1, 501):
    if (F(i)) == 8:
        cnt += 1
print(cnt)