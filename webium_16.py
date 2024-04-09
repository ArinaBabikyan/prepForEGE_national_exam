# def F(n):
#     if n < 3:
#         return 2
#     if n % 2 == 0:
#         return F(n - 2) - F(n - 1) + 2
#     return F(n - 1) - F(n - 2) - 2
# print(F(29))
# def F(n):
#     if n < 3:
#         return 1
#     if n % 2 == 0:
#         return F(n - 1) + n
#     return F(n - 2) + 2 * n
# print(F(23) - F(21))
# from functools import cache
# @cache
# def F(n):
#     if n == 1:
#         return 1
#     return n * F(n - 1) + 1
# print(F(3300))
# print(3303*(3302*(3301*F(3300)+1)+1)+1)
# def F(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 0
#     if n % 2 == 0:
#         return F(n//2) + 1
#     return F(n//2)
#
# for i in range(1000000):
#     if F(i) == 10:
#         print(i)
#         break
print(3 ** 8)