# def ways(s, f):
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return ways(s+1, f) + ways(s * 3, f)
#
# print(ways(5, 49))

# def ways(s, f):
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return ways(s+1, f) + ways(s+2, f) + ways(s * 4, f)
#
# print(ways(1, 13)) # 298
#
# def ways(s, f):
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return ways(s+1, f) + ways(s+3, f)
#
# print(ways(3, 12) * ways(12, 20)) #247

# def ways(s, f):
#     if s == 10:
#         return 0
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return ways(s+1, f) + ways(s*2, f)
#
# print(ways(1, 30)) #68
# def ways(s, f):
#     if s == 12:
#         return 0
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return ways(s+1, f) + ways(s+3, f) + ways(s*2, f)
#
# print(ways(3, 8) * ways(8, 21)) #228

# def ways(s, f):
#     if s == 6:
#         return 0
#     if s == f:
#         return 1
#     if s > f:
#         return 0
#     return ways(s+2, f) + ways(s*3, f)
#
# print(ways(1, 25) * ways(25, 63)) #8