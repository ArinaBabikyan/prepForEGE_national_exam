#23
# import functools
# @functools.cache
# def ways(s, f):
#     if s == f:
#         return 1
#     if s > f or s == 100:
#         return 0
#     if s % 10 == 0:
#         if not s % 68:
#             return ways(s ** 2, f)
#         return ways(s ** 2, f) + ways(s + s % 68, f)
#     if not s % 68:
#         return ways(s ** 2, f) + ways(s + s % 10, f)
#     return ways(s ** 2, f) + ways(s + s % 10, f) + ways(s + s % 68, f)
# print(ways(2, 68), ways(68, 680))
# print(ways(2, 68) * ways(68, 680))
#24
