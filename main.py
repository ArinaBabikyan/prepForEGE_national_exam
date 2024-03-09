"""for n in range(1, 10000):
    n = bin(n)[2:]
    if (n).count('0') == (n).count('1'):
        n = int((n) + (n)[-1])
    else:
        if n.count('0') < n.count('1'):
            n += '0'
        else:
            n += '1'


"""
"""for i in range(99, 1, -1):
    n = bin(i)[2:]
    print(n)
    if n.count('1') == n.count('0'):
        n += n[-1]
    else:
        if n.count('1') > n.count('0'):
            n += '0'
        else:
            n += '1'
    print(n)
    if n.count('1') == n.count('0'):
        n += n[-1]
    else:
        if n.count('1') > n.count('0'):
            n += '0'
        else:
            n += '1'
    if n.count('1') == n.count('0'):
        n += n[-1]
    else:
        if n.count('1') > n.count('0'):
            n += '0'
        else:
            n += '1'
    n10 = int(n, 2)
    print(i, n, n10)
    if n10 % 4 and n10 % 2 == 0:
        print(i)
        break"""
"""from turtle import *
mash = 20
left(90)
for i in range(13):
    right(135)
    forward(5 * mash)
pu()
'''for x in range(10):
    for y in range(10):
        goto(-x * mash - 10, -y * mash - 10)
        dot(5)
for x in range(10):
    for y in range(10):
        goto(x * mash - 10, -y * mash - 10)
        dot(5)'''
done()"""
"""n = 0

flag = False
for i in 'АКРУ':
    for j in 'АКРУ':
        for k in 'АКРУ':
            for p in 'АКРУ':
                for t in 'АКРУ':
                    s = i + j + k + p + t
                    if s == 'РУКАА':
                        flag = True
                    if flag:
                        n += 1
                    if s == 'УКАРА':
                        print(n)
"""
"""s = '7' * 86
while '4444' in s or '7777' in s:
    if '4444' in s:
        s.replace('4444', '77', 1)
    elif '7777' in s:
        s.replace('7777', '44', 1)
print(s)"""
"""for i in range(1, 12938213):
    if (bin(4 ** 2015 + 2 ** i - 2 ** 2015 + 15)[2:]).count('1') == 500:
        print(i)
        break"""
"""
def F(A):
    for x in range(1, 1000):
        if not(not(x % A == 0 and x % 12 == 0) or (x % 42 == 0 or not (x % 12 == 0))):
            return False
    return True


for A in range(1, 1000):
    if F(A):
        print(A)
        break""""""
import functools
@functools.lru_cache()
def F(n,m):
    if m == 0:
        return n
    else:
        return F(m, n % m)
cnt = 0
li = []
for n in range(100, 1001):
    for m in range(100, 1001):
        if n not in li and F(n, m) == 30:
            li.append(n)
print(len(li))
"""
"""li = [((0, 0, 0),)]
while li:
    li1, li = li, []
    for i in li1:
        x, y, z = i[-1]
        res = []
        if x ** 2 + (y + 2) ** 2 + (z + 2) ** 2 <= 147:
            res.append((x, y + 2, z + 2))
        if (x + 1) ** 2 + (y + 1) ** 2 + (z + 1) ** 2 <= 147:
            res.append((x + 1, y + 1, z + 1))
        if (x + 3) ** 2 + (y + 2) ** 2 + z ** 2 <= 147:
            res.append((x + 3, y + 2, z))
        if res:
            for j in res:
                li.append(i + (j,))
        else:
            print(*[(u - a, v - b, w - c) for (a, b, c), (u, v, w)
                    in zip(i, i[1:])])"""
"""n = int(input())
i = 1
while i * 2 <= n:
    print(i, end=' ')
    if i * 4 - 1 >= n:
        print(n - i * 2 + 1, end=' ')
        i *= 2
        break
    i *= 2
# """
#
# import functools
#
#
# @functools.lru_cache()
# def F(s, f):
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return F(s + 2, f) + F(s * 2, f) + F(s * 3, f)
#
#
# print(F(1, 300))
#
# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not(x == z) or (not y or w)) == (not((not w or z) or (not x or y))):
#                     print(x, y, z, w)

# with open("3.txt") as line, open("33.txt") as lene:
#     a = line.readlines()
#     arr = [list(map(int, i.strip().split())) for i in lene.readlines()]
#     d = {}
#     for i in range(len(arr)):
#         if a[i] in d.keys():
#             d[a[i]] += arr[i][0] * arr[i][1]
#         else:
#             d[a[i]] = arr[i][0] * arr[i][1]
#     count = 0
#     print(d)
#     for v in d.values():
#         if v > 200000:
#             count += 1
#     print(count)

# count = set()
# for n in range(500000000, 800000009):
#     a = int(bin(n)[2:] + bin(n%4)[2:], 2)
#     print(a)
#     if 1100000000 <= a <= 1987653210:
#         count.add(a)
# print(len(count))

# import turtle as t
#
# t.left(90)
# k = 10
# t.up()
#
# for x in range(20):
#     for y in range(20):
#         t.goto(x*k, y*k)
#         t.dot(2)
# t.goto(0, 0)
# t.down()
# for i in range(4):
#     for j in range(4):
#         t.forward(8*k)
#         t.right(90)
#         input()
#     t.forward(13*k)
#     t.right(90)
#     t.forward(4*k)
#     input()
# input()


# def solve(n):
#     res = ""
#     while n > 0:
#         res += str(n % 9)
#         n //= 9
#     return res[::-1]
#
#
# count = 0
# for i in range(3485457999, 32000000000):
#     if len(solve(i)) == 11:
#         print(i)
#         break
#     print(len(solve(i)))
# print(count)

# with open("t.txt") as line:
#     fcount = 0
#     arr = [list(map(int, i.strip().split())) for i in line.readlines()]
#     d = {}
#     for i in range(len(arr)):
#         count = 0
#         for j in range(6):
#             if arr[i].count(arr[i][j]) == 1:
#                 lcount = 0
#                 if (arr[i][j], j) in d.keys():
#                     if d[(arr[i][j], j)] > 170:
#                         count -= 1
#                 else:
#                     for k in range(len(arr)):
#                         if arr[k][j] == arr[i][j]:
#                             lcount += 1
#                         if lcount >= 170:
#                             lcount = 1000
#                             count -= 1
#                             break
#                     d[(arr[i][j], j)] = lcount
#                 count += 1
#         if count >= 4:
#             fcount += 1
#     print(fcount)

# print(600*1024/1600/8)
#
# print(bin(20))
# print(bin(27))
# print(2**14)

# for p in range(2, 100):
#     for x in range(p):
#         for y in range(p):
#             for z in range(p):
#                 for w in range(p):
#                     if z * p ** 4 + x * p ** 3 + y * p ** 2 + x * p + 4 + x * p ** 4 + y * p ** 3 + 6 * p ** 2 +\
#                             5 * p + 8 == w * p ** 4 + z * p ** 3 + x * p ** 2 + 7 * p + 3:
#                         print(x, y, z, w, p)
#
# for A in range(16640, 100000):
#     flag = True
#     for x in range(100000):
#         if not(not(x & 20777 != 0) or (not(x & 12332 == 0) or (x & A != 0))):
#             flag = False
#             break
#     if flag:
#         print(A)
#
# from functools import lru_cache
#
#
# @lru_cache()
# def F(n):
#     if n == 0:
#         return 1
#     if n & 1:
#         return (n%10) * F(n//100)
#     return F(n//100)
#
#
# count = 0
# for k in range(10000000, 90000000):
#     if F(k) == 25:
#         count += 1
# print(count)

# def game(s, n):
#     if s < 12:
#         return n % 2 == 0
#     if n == 0:
#         return 0
#     if s % 2 == 0 and s % 3 == 0:
#         h = [game(s-1, n-1), game(s//2, n-1), game(s//3, n-1)]
#     else:
#         if s % 2 == 0:
#             h = [game(s-1, n-1), game(s//2, n-1)]
#         if s % 3 == 0:
#             h = [game(s - 1, n - 1), game(s // 3, n - 1)]
#         h = [game(s-1, n)]
#     return any(h) if n % 2 else all(h)
#
#
# for w in range(12, 6000):
#     if not game(w, 1) and (game(w, 2) or game(w, 4)):
#         print(w)

# with open("7.txt") as line:
#     arr = list(map(int, line.readlines()))
#     m = 3832
#     count = []
#     for i in range(len(arr)-2):
#         res = (arr[i], arr[i+1], arr[i+2])
#         count1 = 0
#         count5 = 0
#         count3 = 0
#         for n in range(3):
#             if len(str(res[n])) == 4:
#                 count1 += 1
#             if res[n] % 5 == 0:
#                 count5 += 1
#             if res[n] % 3 == 0:
#                 count3 += 1
#         if 1 <= count1 < 3 and count3 < count5 and sum(res) > m:
#             count.append(sum(res))
#     print(len(count))
#     print(max(count))
#
# def solve(s, f, flag):
#     if s > f:
#         return 0
#     if s == f:
#         return 1
#     if flag:
#         return solve(s-1, f, False) + solve(s+3, f, True) + solve(s*2, f, True)
#     return solve(s+3, f, True) + solve(s*2, f, True)
#
#
# print(solve(3, 12, True))
#
# for i in range(10):
#     for j in range(1000):
#         n = (3-len(str(j))) * "0" + str(j)
#         a = int(f'1{n}4182{i}7')
#         if a % 1991 == 0:
#             print(a)
#
# with open("7.txt") as line:
#     arr = sorted([list(map(int, i.strip().split())) for i in line.readlines()[1:]])
#     mg = [0, 0, 0, 0, 0, 0]
#     counts = [0, 0, 0, 0, 0, 0]
#     expired = 0
#     for i in arr:
#         if mg[i[2]-1] <= i[0]:
#             mg[i[2]-1] = i[0] + i[1]
#             counts[i[2]-1] += 1
#         else:
#             if mg[i[2]-1] > i[0] + 40:
#                 expired += 1
#             else:
#                 mg[i[2]-1] += i[1]
#                 counts[i[2] - 1] += 1
#     print(expired)
#     print(max(counts))

with open("7.txt") as line:
    arr = list(map(int, line.readlines()))
    count = []
    for i in range(len(arr)-2):
        for j in range(i, len(arr)-1):
            for k in range(j, len(arr)):
                res = (arr[i], arr[j], arr[k])
                if sum(res) % 105 == 0:
                    count.append(sum(res))
    print(max(count))