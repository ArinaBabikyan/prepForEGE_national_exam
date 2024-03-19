# print('y z w x f')
# for x in [0, 1]:
#     for y in [0,1 ]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 f = int(((not y or w) == (not x or not z)) and (x or w))
#                 print(y,z,w,x, f)

# 5
# cnt = 0
# for n in range(100, 1000):
#     li = sorted(list(str(n)))
#     if '0' not in li:
#         k = (int(''.join(li[-2:][::-1])) - int(''.join(li[0:2])))
#         print((int(''.join(li[-2:][::-1])), int(''.join(li[0:2]))), n)
#     else:
#         k = (int(''.join(li[-2:][::-1])) - int(li[1] + li[0]))
#     if k == 58:
#         cnt += 1
#         print(n)
# print(cnt)

# 6
# import turtle as t
# t.left(90)
# mash = 10
# for i in range(6):
#     t.forward(25 * mash)
#     t.right(120)
# t.up()
# t.forward(20 * mash)
# t.left(90)
# t.back(5 * mash)
# t.down()
# for i in range(2):
#     t.forward(20 * mash)
#     t.left(90)
#     t.forward(10 * mash)
#     t.left(90)
# t.up()
# t.goto(0, 10 * mash)
# t.speed(100)
# for x in range(7):
#     for y in range(25):
#         t.goto(x * mash, y * mash)
#         t.dot(3)
# input()
# 8
# li = ['А', "Г", "Д", "И", "Л", "Н", "Р", 'Я']
# cnt = 1
# for i in li:
#     for j in li:
#         for k in li:
#             for m in li:
#                 for a in li:
#                     for b in li:
#                         s = i + j + k + m + a + b
#                         if not cnt % 2 and i != "Я" and s.count('Д') == 3:
#                             print(cnt, s)
#                         cnt += 1
# with open('9') as f:
#     li = [list(map(int, s.split())) for s in f.readlines()]
#     res = 0
#     for i in li:
#         cnt = 0
#         ma = 0
#         mi = 9999999999999
#         k = 0
#         for j in range(7):
#             if i.count(i[j]) == 2:
#                 cnt += 1
#                 ma = max(ma, i[j])
#                 mi = min(ma, i[j])
#             else:
#                 k = i[j]
#         if cnt == 6:
#             if (ma + mi) / 2 < k:
#                 print(i)
#                 res += 1
#     print(res)

# 12
ma = -1
for i in range(91, 1000):
    s = '1' * i
    while '111' in s:
        s = s.replace('111', '2', 1)
        if '2222' in s:
            s = s.replace('2222', '333', 1)
        if '33' in s:
            s = s.replace('33', '1', 1)
    n = s.count('1')
    if n > ma:
        ma = n
        print(ma, i)

# print(bin(192)[2:] + bin(168)[2:] + bin(32)[2:] + bin(48)[2:])
# print('00'+ bin(48)[2:])
# print(bin(240)[2:])
# cnt= 0
# for i in [0, 1]:
#     for j in [0, 1]:
#         for a in [0, 1]:
#             for b in [0, 1]:
#                 if (i + j + a + b) % 2:
#                     cnt += 1
#                     print(i, j, a, b)
# print(cnt)
#14
# print(bin(1024 - 511))
# print(bin(1024))
#15
# def f(n):
#     for x in range(1000):
#         for y in range(1000):
#             if not ((x > 10) or (x * x < n)) or not((y * y >=  n) or (y <= 10)):
#                 return False
#     return True
#
# cnt = 0
# for i in range(10000):
#     if f(i):
#         cnt += 1
# print(cnt)
# 16
# def F(n):
#     if n <= 18:
#         return n + 3
#     if n % 3 == 0:
#         return (n // 3) * F(n // 3) + n - 12
#     return F(n - 1) + n * n + 5
# cnt = 0
# for i in range(1, 1001):
#     k = F(i)
#     flag = True
#     for j in str(k):
#         if int(j) % 2:
#             flag = False
#     if flag:
#         cnt += 1
# print(cnt)
# 17
# ma = 0
# cnt = 0
# for i in range(198372, 876193):
#     if i % sum(list(map(int, str(i)))) == 11:
#         ma = max(ma, i)
#         cnt += 1
# print(cnt, ma)
# 22
# with open('22') as f:
#     li =
# 23

# def ways(s, f):
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return ways(s + 1, f) + ways(s + 2, f) + ways(s + s - 1, f)
#
# print(ways(2, 9))

# 24
# f = open('24')
# s = f.readline()
# a = 'AB'
# print(a * 12)
# for i in range(1000000, 1, -1):
#     if a * i in s:
#         print(i)
#         break
# with open('26') as f:
#     li = f.readlines()
#     s, n = list(map(int, li.pop(0).split()))
#     li = [int(i) for i in li]
#     li = sorted(li)
#     su = 0
#     cnt = 0
#     for i in li:
#         if su + i <= s:
#             su += i
#             cnt += 1
#     print(li)
#     print(li[cnt - 2])
#     print(sum(li[:cnt]) - li[cnt] - li[cnt - 1] + li[-1] + li[-2] - li[cnt - 2] + 73)
#     print(cnt, li[-1])
# with open('27a') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     mi = 9999999
#     for i in range(n - 6):
#         for j in range(i + 6, n):
#             if li[i] * li[j] % 2:
#                 mi = min(mi, li[i] * li[j])
#     print(mi)
# with open('27b') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     mi = 9999999
#     mi2 = 9999999
#     for i in range(6, n):
#         if li[i - 6] % 2:
#             mi = min(mi, li[i - 6])
#         if li[i] % 2:
#             mi2 = min(mi2, mi * li[i])
#     print(mi2)