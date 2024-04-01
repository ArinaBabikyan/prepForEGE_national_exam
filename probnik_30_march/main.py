# 6
# def troich(n):
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
#
# for i in range(1, 10000):
#     r = troich(i)
#     if i % 2:
#         r += troich(sum(list(map(int, list(r)))))
#     else:
#         r = '1' + r + '00'
#     if int(r, 3) > 168:
#         print(i)
#         break
# 7
# import turtle as t
# t.left(90)
# mash = 1
# for i in range(12):
#     for j in range(8):
#         t.forward(50 * mash)
#         t.right(45)
#     t.right(30)
# input()

# 8
# print(80*2**23/(205*2*80000))

# 9
# from itertools import permutations
# glas = 'ИАЕ'
# res = 0
# for i in permutations('Т, И, М, А, Ш, Е, В, С, К'.split(', '), 6):
#     cnt = 0
#     flag = True
#     for j in range(len(i)):
#         if i[j] in glas:
#             cnt += 1
#             if j >= 1:
#                 if i[j - 1] == 'Ш':
#                     flag = False
#             if j < len(i) - 1:
#                 if i[j + 1] == 'Ш':
#                     flag = False
#     if cnt == 3 and flag:
#         res += 1
#         print(i)
# print(res)

# 10
# with open('10') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     for i in li:
#         cnt = 0
#         for j in i:
#             if i.count(j) == 1:
#                 cnt += 1
#         if cnt == 2:
#             if i.count(max(i)) == 1:
#                 if (max(i) + min(i)) >= sum(i) - (max(i) + min(i)):
#                     print(i, li.count(i), sum(i))
#                     break


# 11
# print((11 + 120) * 20)

# 12
# for i in range(200, 10000):
#     s = '1' * i
#     while '111' in s or '222' in s:
#         if '111' in s:
#             s = s.replace('111', '22', 1)
#         if '222' in s:
#             s = s.replace('222', '1', 1)
#     if '2' not in s:
#         print(i)
#         break


# 13
# import ipaddress
# cnt = 0
# for i in range(255):
#     if ipaddress.ip_address(f'136.36.240.{i}') in ipaddress.IPv4Network('136.36.240.16/255.255.255.248'):
#         if '101' not in (bin(240)[2:] + bin(i)[2:]):
#             cnt += 1
#             print(bin(i)[2:].zfill(8))
# print(cnt)
# print( bin(136)[2:] + bin(36)[2:] + (bin(240)[2:]))

# 14
# print(str(8 ** 740 - 2 ** 900 + 7).count('0'))

# 15
# def f(A):
#     for x in range(10000):
#         if not ((x & 30 != 4) or (not (x & 35 == 1) or (x & A == 0))):
#             return False
#     return True
#
# for i in range(10000, 1, -1):
#      if f(i):
#          print(i)

# 16
# def F(n):
#     if n <= 3:
#         return n
#     if n <= 32:
#         return n // 4 + F(n - 3)
#     return 2 * F(n - 5)
#
# print(F(100))

# 17
# with open('17') as f:
#     li = [int(i) for i in f.readlines()]
#     li_chet = list(filter(lambda x: x % 2 == 0, li))
#     key = sum(li_chet) / len(li_chet)
#     ma = 0
#     cnt = 0
#     for i in range(1, len(li)):
#         x, y = li[i - 1], li[i]
#         if x % 3 == 0 or y % 3 == 0:
#             if x < key or y < key:
#                 ma = max(ma, x + y)
#                 cnt += 1
#     print(cnt, ma)


# 23
# def ways(s, f):
#     if s == f:
#         return 1
#     if s < f:
#         return 0
#     return ways(s - 2, f) + ways(s - 5, f)
#
# print(ways(23, 2))

# 24
# with open('24.txt') as f:
#     s = f.readline()
#     cnt = 0
#     for i in range(5, len(s)):
#         if s[i - 5:i] == s[i - 5:i][::-1]:
#             print(s[i - 5:i])
#             cnt += 1
#     print(cnt)
# 25
# import math
#
# def find_divisors(n):
#     divisors = []
#     for i in range(1, int(math.sqrt(n))+1):
#         if n % i == 0:
#             divisors.append(i)
#             if i != n // i:
#                 divisors.append(n // i)
#     return divisors
#
# for i in range(164700, 164753):
#     divs = find_divisors(i)
#     if len(divs) == 6:
#         print(sorted(divs)[-2:])


# 26
# with open('26.txt') as f:
#     li = f.readlines()
#     n, k = list(map(int, li.pop(0).split()))
#     li = sorted([int(i) for i in li])
#     print(sum(li[-k:]))
#     print(li[-k:][0])


# 27
# with open('27-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ma = 0
#     length = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if sum(li[i:j]) % 89 == 0 and sum(li[i:j]) % (j - i + 1) == 0:
#                 if ma < sum(li[i:j]):
#                     ma = sum(li[i:j])
#                     length = j - i + 1
#                 if ma == sum(li[i:j]) and j - i + 1 <= length:
#                     length = j - i + 1
#     print(length)
# with open('27-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ma = 0
#     length = 0
#     sums = [li[0]]
#     osts = [[]] * 89
#     for i in range(1, n):
#         sums[i] = sums[i - 1] + li[i]
#         osts[sums[i] % 89].append(sums[i])
#     for i in range(89):
#         temp = sorted(osts[i])
