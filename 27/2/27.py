# 1 A
# with open('27.1-A.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     res = 10 ** 20
#     ost = [0] * 3
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if (li[i] + li[j] + li[k]) % 3 == 0:
#                     res = min(res, (li[i] + li[j] + li[k]))
#     print(res)
# B
# with open('27.1-B.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     res = 10 ** 20
#     pairs = [10 ** 20] * 3
#     ost = [10 ** 20] * 3
#     for i in range(n):
#         p = (-li[i]) % 3
#         res = min(res, li[i] + pairs[p])
#         for j in ost:
#             new_pair = j + li[i]
#             pairs[new_pair % 3] = min(pairs[new_pair % 3], new_pair)
#         ost[li[i] % 3] = min(ost[li[i] % 3],  li[i])
#     print(res)
# 2
# A
# with open('27.2-A.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     k = li.pop(0)
#     n = li.pop(0)
#     ost = [0, 0]
#     res = 0
#     for i in range(n):
#         for j in range(i + k, n):
#             if (li[i] + li[j]) % 2:
#                 res = max(res, (li[i] + li[j]))
#     print(res) #9989
# B
# with open('27.1-B.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     k = li.pop(0)
#     n = li.pop(0)
#     ost = [0, 0]
#     res = 0
#     for i in range(k, n):
#         if li[i] % 2:
#             res = max(res, (li[i] + ost[0]))
#         else:
#             res = max(res, (li[i] + ost[1]))
#         ost[li[i - k] % 2] = max(li[i - k], ost[li[i - k] % 2])
#     print(res) #9989
# 3
# A
# from itertools import combinations
#
# with open('27.3-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     res = 0
#     for a in range(1, n + 1):
#         for i in combinations(li, a):
#             if sum(i) % 3 == 0:
#                 res += 1
#     print(res) # 351


# B
# with open('27.3-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     res = 0
#     ost = [0] * 25
#     for i in li:
#         old = ost[:]
#         for j in range(3):
#             if old[j] > 0:
#                 ost[(i + j) % 3] += old[j]
#         ost[i % 3] += 1
#         print(ost, i)
#     print(ost[0])


# 4
from itertools import combinations

# with open('27.4-A.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ma = 0
#     for a in range(1, n + 1):
#         for i in combinations(li, a):
#             if sum(i) % 25 == 0:
#                 ma = max(sum(i), ma)
#     print(ma) # 351
# f = open('27.3-B')
# a = [int(i) for i in f.readlines()]
# n = a.pop(0)
# m = 25
# sumi = [0] * m
# for x in a:
#     old = sumi[:]
#     for s in old:
#         if s > 0:
#             new_s = s + x
#             sumi [new_s % m] = max (sumi[new_s % m], new_s)
#     sumi[x % m] = max (sumi[x % m], x)
# print(sumi[0])



# 58 reshu-ege
with open('27-A.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    li = [int(i) for i in f.readlines()]
    su1 = []
    su_max_left = 0
    max_left = 0
    su_max_left3 = 0
    for i in range(2 * k, n - k):
        max_left = max(max_left, li[i - 4 * k])
        su_max_left = max(li[i - 2 * k] + max_left, su_max_left)
        su_max_left3 = max(su_max_left3, su_max_left)
    print(su_max_left3)