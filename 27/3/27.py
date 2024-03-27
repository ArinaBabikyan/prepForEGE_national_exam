# 1.A
# with open('27.1-A.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ma = 0
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             if sum(li[i:j]) % 1000 == 0:
#                 ma = max(ma, sum(li[i:j]))
#     print(ma)

# 1.B
# with open('27.1-B.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ma = 0
#     sums = [[] for i in range(1000)]
#     cur_sum = 0
#     for i in range(n):
#         cur_sum += li[i]
#         sums[cur_sum % 1000].append(cur_sum)
#     for i in sums:
#         if i:
#             ma = max(ma, max(i) - min(i))
#     print(ma)
# 2.A
# with open('27.2-A.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ma = 0
#     res = {}
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             if sum(li[i:j]) % 89 == 0:
#                 if sum(li[i:j]) >= ma:
#                     ma = sum(li[i:j])
#                     if ma not in res.keys():
#                         res[ma] = j - i
#                     else:
#                         res[ma] = min(res[ma], j - i)
#     print(ma, res[ma])
# 2.B
# with open('27.2-B.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ma = 0
#     sums = [[] for i in range(89)]
#     cur_sum = 0
#     indxs = [[] for i in range(89)]
#     for i in range(n):
#         cur_sum += li[i]
#         sums[cur_sum % 89].append(cur_sum)
#         indxs[cur_sum % 89].append(i)
#     res = 10 ** 10
#     for k in range(89):
#         i = sums[k]
#         if i:
#             if i[-1] - i[0] > ma:
#                 ma = i[-1] - i[0]
#                 res = indxs[k][-1] - indxs[k][0]
#             elif i[-1] - i[0] == ma:
#                 res = min(res, indxs[k][-1] - indxs[k][0])
#     print(ma, res)
# 3-A
# with open('27.3-A.txt') as f:
#     li = f.readlines()
#     n, m = list(map(int, li.pop(0).split()))
#     cnt = 0
#     li = [int(i) for i in li]
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             su = 1
#             for a in range(i, j):
#                 su *= li[a]
#             if su % m:
#                 cnt += 1
#     print(cnt)
# 3-B
# with open('27.3-B.txt') as f:
#     li = f.readlines()
#     n, m = list(map(int, li.pop(0).split()))
#     cnt = 0
#     li = [int(i) for i in li]
#     su_cur = 1
#     sums = [1 for i in range(n)]
#     pointer = 0
#     for k in range(n):
#         i = li[k]
#         su_cur *= i
#         while su_cur % m == 0:
#             if pointer > k:
#                 break
#             su_cur //= li[pointer]
#             pointer += 1
#         else:
#             cnt += k - pointer + 1
#     print(cnt)
# 5.A
# with open('27.5-A.txt') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     cnt = 0
#     for i in range(n):
#         for j in range(i + 101, n + 1):
#             if sum(li[i:j]) % 999 == 0:
#                 cnt += 1
#     print(cnt)

with open('27.5-B.txt') as f:
    li = [int(i) for i in f.readlines()]
    n = li.pop(0)
    cnt = 0
    su_cur = 0
    m = 999
    osts = [[] for i in range(m)]
    indxs = [[] for i in range(m)]
    for k in range(n):
        i = li[k]
        su_cur += i
        osts[su_cur % m].append(su_cur)
        indxs[su_cur % m].append(k)
        if len(indxs[su_cur % m]) >= 2:
            for a in indxs[su_cur % m]:
                if k - a >= 100:
                    cnt += 1

    cnt += 1
    print(indxs)
    print(cnt)