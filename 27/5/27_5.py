# # Автодороги
# # 1
# with open('27.1-A.txt') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     n, m = li.pop(0)
#     di = {}
#     cont = 30
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 0
#     for i in di:
#         su = 0
#         for j in di:
#             distance = abs(j - i)
#             if distance > m:
#                 continue
#             su += di[j]
#         # print(i, su)
#         res = max(su, res)
#     print(res)
# with open('27.1-B.txt') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     n, m = li.pop(0)
#     di = {}
#     cont = 30
#     di = [0] * (1 + max(list(map(lambda x: x[0], li))))
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 0
#     su = sum(di[:2*m + 1])
#     for i in range(m, len(di) - m - 1):
#         if di[i]:
#             res = max(res, su)
#         # print(i, su, di, di[i-m], di[i + m])
#         su -= di[i - m]
#         su += di[i + m + 1]
#     # for i in range(m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     # for i in range(len(li) - m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     print(res)
#
# Автодороги
# 2
# with open('27.2-A') as f:
#     n, m = list(map(int, (f.readline().split())))
#     li = []
#     cnt = 1
#     for i in f.readlines():
#         li.append([cnt, int(i)])
#         cnt += 1
#     di = {}
#     cont = 1
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 0
#     for i in di:
#         su = 0
#         for j in di:
#             distance = abs(j - i)
#             if distance > m:
#                 continue
#             su += di[j]
#         # print(i, su)
#         res = max(su, res)
#     print(res)
#
# with open('27.2-B.txt') as f:
#     n, m = list(map(int, (f.readline().split())))
#     li = []
#     cnt = 1
#     for i in f.readlines():
#         li.append([cnt, int(i)])
#         cnt += 1
#     di = [0] * (1 + max(list(map(lambda x: x[0], li))))
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 0
#     su = sum(di[:2*m + 1])
#     for i in range(m, len(di) - m - 1):
#         if di[i]:
#             res = max(res, su)
#         # print(i, su, di, di[i-m], di[i + m])
#         su -= di[i - m]
#         su += di[i + m + 1]
#     # for i in range(m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     # for i in range(len(li) - m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     print(res)
#
#
#
# 3
# with open('27.3-A.txt') as f:
#     n, m = list(map(int, (f.readline().split())))
#     li = []
#     cnt = 1
#     cont = 1
#     for i in f.readlines():
#         li.append(int(i))
#         cnt += 1
#     li[0:0] = li[len(li) - m:len(li)]
#     li.extend(li[:m])
#     print(li)
#     di = li.copy()
#     res = 0
#     su = sum(di[:2*m + 1])
#     for i in range(m, len(di) - m - 1):
#         if di[i]:
#             res = max(res, su)
#         # print(i, su, di, di[i-m], di[i + m])
#         su -= di[i - m]
#         su += di[i + m + 1]
#     # for i in range(m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     # for i in range(len(li) - m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     print(res)
# 4
# with open('27.4-B') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     n, m = li.pop(0)
#     di = {}
#     cont = m
#     m = n
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 10 ** 1000
#     for i in di:
#         su = 0
#         for j in di:
#             distance = abs(j - i)
#             su += di[j] * distance
#         # print(i, su)
#         res = min(su, res)
#     print(res)
# with open('27.4-B') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     n, m = li.pop(0)
#     di = {}
#     cont = m
#     m = n
#     di = {}
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 10 ** 1000
#     punct = 0
#     print(di)
#     su = sum([abs(i - punct) * di[i] for i in di])
#     left = 0
#     right = sum(di[i] for i in di)
#     for i in di:
#         su += left * abs(i - punct)
#         su -= right * abs(i - punct)
#         res = min(res, su)
#         # print(su, i, left)
#         right -= di[i]
#         left += di[i]
#         punct = i
#
#     # for i in range(m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     # for i in range(len(li) - m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     print(res)
# 5
# with open('27.5-A') as f:
#     n = int(f.readline())
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     m = 100
#     di = {}
#     cont = m
#     m = n
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 10 ** 1000
#     for i in di:
#         su = 0
#         for j in di:
#             distance = abs(j - i)
#             su += di[j] * distance
#         # print(i, su)
#         res = min(su, res)
#     print(res)
# with open('27.5-B') as f:
#     n = int(f.readline())
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     m = 100
#     di = {}
#     cont = m
#     m = n
#     di = {}
#     for i in li:
#         di[i[0]] = i[1] // cont + int(bool(i[1] % cont))
#     res = 10 ** 1000
#     punct = 0
#     print(di)
#     su = sum([abs(i - punct) * di[i] for i in di])
#     left = 0
#     right = sum(di[i] for i in di)
#     for i in di:
#         su += left * abs(i - punct)
#         su -= right * abs(i - punct)
#         res = min(res, su)
#         # print(su, i, left)
#         right -= di[i]
#         left += di[i]
#         punct = i
#
#     # for i in range(m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     # for i in range(len(li) - m):
#     #     res = max(sum(di[i:i + m + 1]), res)
#     print(res)
# 6
with open('27.6-B') as f:
    li = [list(map(int,i.split())) for i in f.readlines()]
    n, m, k = li.pop(0)
    ma = 0
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            ma = max(ma, sum(list(map(lambda x: sum(x[j:j+k]), li[i:i + k]))))
    print(ma)


# with open('27.6-B') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     n, m, k = li.pop(0)
#     ma = 0
#     li2 = []
#     for i in range(n):
#         for j in range(m):
#             li2[i][j] = li[i][j] + li[i][j-1]
