# 2
# print("x y z w f")
# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 print(x, y, z, w, int((not x or y or (z == x)) and (not w or z)))
# 4
# def chet(o):
#     res = ''
#     while o > 0:
#         res += str(o % 4)
#         o //= 4
#     return res[::-1]
#
# for n in range(1000, 0, -1):
#     s = chet(n)
#     if len(s) % 2 == 0:
#         s = s[:len(s) // 2] + '0' + s[len(s) // 2:]
#     if int(s) <= 180:
#         print(n)
#         print(s)
#         break


# 5
# import turtle as t
# t.left(90)
# t.right(60)
# mash = 30
# for i in range(2):
#     t.forward(7 * mash)
#     t.right(120)
# t.right(300)
# t.forward(7 * mash)
# for i in range(2):
#     t.right(60)
#     t.forward(7 * mash)
#     t.right(60)
# t.up()
# t.speed(100)
# for x in range(7):
#     for y in range(5):
#         t.goto(x * mash, y * mash)
#         t.dot(3)
# for x in range(7):
#     for y in range(10):
#         t.goto(-x * mash, -y * mash)
#         t.dot(3)
# for x in range(7):
#     for y in range(10):
#         t.goto(x * mash, -y * mash)
#         t.dot(3)
# input()
# print(600 * 800 * 3 / 180)
# 8
# li = ['А', "Г", "Д", "И", "Л", "Н", "Р", "Я"]
# cnt = 1
# for i in li:
#     for j in li:
#         for k in li:
#             for a in li:
#                 for b in li:
#                     for c in li:
#                         if not cnt % 2:
#                             if i != "Я":
#                                 s = i + j + k + a + b + c
#                                 if s.count('Д') == 3:
#                                     print(cnt, s)
#                         cnt += 1

#11
# print(96000 / 300 - 57)
# print(bin(240)[2:])
# print(2 ** 12 - 2 )
# 14
# li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# for x in li:
#     if (int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)) % 18 == 0:
#         print((int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)) / 18)
#         break
# 15
# def f(A):
#     for x in range(1000):
#         if not ((x & A == 0) or not(x & 37 == 0) or not(x & 12 == 0)):
#             return False
#     return True
#
# for i in range(1000, 1, -1):
#     if f(i):
#         print(i)


# 16
# def F(n):
#     return G(n - 1)
#
# def G(n):
#     if n < 10:
#         return n
#     return G(n - 2) + 1
#
# cnt = 0
# li = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for n in range(1, 101):
#     if F(n) in li:
#         # print(n)
#         cnt += 1
#
# print(cnt)
# 17
with open('17') as f:
    li = [int(i) for i in f.readlines()]
    ma = 0
    pairs = []
    for i in li:
        if len(str(i)) == 4 and i % 100 == 39:
            ma = max(ma, i)
    print(ma)
    for i in range(1, len(li)):
        a, b = li[i - 1], li[i]
        if (len(str(abs(a))) == 4) != (len(str(abs(b))) == 4):
            print(a, b)
            if (a + b) ** 2 <= ma ** 2:
                pairs.append([a, b])
    print(pairs)
    print(len(pairs))
    print(sum(max(pairs, key=lambda x: sum(x))))
# 23
# def ways(s, f, cnt):
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     if cnt == 1:
#         return ways(s + 2, f, cnt + 1) + ways(s + 3, f, cnt + 1)
#     return ways(s + 2, f, cnt + 1) + ways(s + 3, f, cnt + 1) + ways(s * 2, f, cnt + 1)
# print(ways(5, 30, 1))
# 24
# with open('b715458d-ba8c-47f6-8faf-c3aeb5451407.txt') as f:
#     s = f.readline()
#     print(max(s.count('RSQ'), s.count('RQS'), s.count('QRS'), s.count('QSR'), s.count('SRQ'), s.count('SQR')) * 3)

# 25
# f = open('output.txt', 'w')
# import re
# for i in range(21025, 10 ** 10 + 1, 21025):
#     if re.fullmatch('12.{0,10}34.{1}5', str(i)):
#         li = list(map(lambda x: int(x)%2, list(str(i))))
#         if li.count(1) == li.count(0):
#             print(i, i / 21025, file=f)

# 26
# with open('26.txt') as f:
#     li = f.readlines()
#     s, n = list(map(int, li.pop(0).split()))
#     li = sorted([int(i) for i in li])
#     res = 0
#     for i in range(n, 0, -1):
#         if sum(li[:i]) <= s:
#             res = i
#             break
#     su_res = (sum(li[:res]))
#     print(res)
#     print(s - su_res + li[res - 1])
#     print(li)

# 27
# with open('27a') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     su = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if sum(li[i:j]) % 113 == 0:
#                 su = max(su, sum(li[i:j]))
#                 print(su, i, j)
#     print(su)
# with open('f5ecff8a-7231-40ea-b396-ab89ac709468.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     su = sum(li)
#     ost = 42
#     ost_su = [[] for i in range(113)]
#     su_cur = 0
#     ind = [[] for i in range(113)]
#     for i in range(n):
#         su_cur += li[i]
#         ost_su[su_cur % 113].append(su_cur)
#         ind[su_cur % 113].append(i)
#     res = 0
#     length = 0
#     for i in range(113):
#         if max(ost_su[i]) - min(ost_su[i]) > res:
#             res = max(ost_su[i]) - min(ost_su[i])
#             length = max(ind[i]) - min(ind[i])
#     print(res, length)
