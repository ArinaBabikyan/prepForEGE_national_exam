# 1
# файл А
# with open("27.1-A") as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     res = 0
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             x = li[i:j]
#             if len(list(filter(lambda y: y % 5 == 0, x))) % 11 == 0 and len(list(filter(lambda y: y % 5 == 0, x))) > 0:
#                 res += 1
#     print(res)

# эффективное решение
# with open("27.1-B") as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     res = 0
#     temp = [0] * n
#     osts = [0] * 11
#     for i in range(n):
#         x = li[i]
#         temp[i] = temp[i-1] + int(x % 5 == 0)
#     for i in range(11, max(temp) + 1):
#         for j in range(i // 11):
#             res += temp.count(i) * temp.count(i - 11 * (j + 1))
#     for i in range(11, max(temp) + 1, 11):
#         res += temp.count(i)
#     print(res)


# 2
# file A
# with open('27.2-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     chet = 0
#     nechet = 0
#     res = 0
#     ma = 0
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             x = list(map(lambda y: y % 2, li[i:j]))
#             if sum(x) == len(x) / 2:
#                 res += 1
#                 ma = max(ma, len(x))
#     print(res,ma)

# эффективное решение
# with open('27.2-B') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     chet = 0
#     nechet = 0
#     res = 0
#     x = []
#     ma = 0
#     balances = {}
#     for i in range(n):
#         elem = li[i]
#         chet += int(elem % 2 == 0)
#         nechet += elem % 2
#         balance = chet - nechet
#         if balance in balances:
#             balances[balance] = min(balances[balance], i)
#         else:
#             balances[balance] = i
#         ma = max(ma, i - balances[balance])
#         x.append(balance)
#     print(ma)

# 3
# with open('27.3-A') as f:
#     n, m = list(map(int, f.readline().split()))
#     li = [int(i) for i in f.readlines()]
#     res = 0
#     su = sum(li)
#     for i in range(n):
#         su -= li[i]
#         su1 = su
#         for j in range(n - 1, i, -1):
#             su1 -= li[j]
#             if su1 <= m:
#                 res = max(res, j - i)
#     print(res - 1)
# with open('27.3-B') as f:
#     n, m = list(map(int, f.readline().split()))
#     li = [int(i) for i in f.readlines()]
#     res = 0
#     su = 0
#     sums = [0] * n
#     ma = 0
#     key = 0
#     for i in range(n):
#         su += li[i]
#         sums[i] = su
#         for j in range(key, i):
#             if su - sums[j] <= m:
#                 ma = max(ma, i - j)
#                 key = j
#                 break
#     print(ma)


# 5
with open('27.5-A') as f:
    n, d = list(map(int, f.readline().split()))
    li = [int(i) for i in f.readlines()]
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] == li[j]:
                if sum(li[i + 1:j]) % d == 0 and sum(li[i + 1:j]):
                    cnt += 1
    print(cnt)
with open('27.5-B') as f:
    n, d = list(map(int, f.readline().split()))
    li = [int(i) for i in f.readlines()]
    cnt = 0
    di = {}
    sums = [0] * n
    su = 0
    for i in range(n):
        x = li[i]
        su += x
        sums[i] = su
        if x not in di:
            di[x] = [i]
        else:
            for j in di[x]:
                if (sums[i - 1] - sums[j]) % d == 0 and (sums[i - 1] - sums[j]):
                    cnt += 1
            di[x].append(i)
    print(cnt)


