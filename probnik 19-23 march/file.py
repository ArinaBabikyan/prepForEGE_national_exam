# 5
# for n in range(1000):
#     s = bin(n)[2:]
#     if n % 3 == 0:
#         s += s[-3:]
#     else:
#         s += bin(n % 3 * 3)[2:]
#     if int(s, 2) > 76:
#         print(n)
#         break
#
# for n in range(1000, 0, -1):
#     s = bin(n)[2:]
#     if n % 3 == 0:
#         s += s[-3:]
#     else:
#         s += bin(n % 3 * 3)[2:]
#     if int(s, 2) < 100:
#         print(n)
#         break
# 6
# import turtle as t
# t.left(90)
# mash = 20
# t.right(45)
# for i in range(7):
#     t.forward(6 * mash)
#     t.right(45)
#     t.forward(12 * mash)
#     t.right(135)
#
# t.up()
# for x in range(20):
#     for y in range(7):
#         t.goto(x * mash, y * mash)
#         t.dot(3)
# input()
# print(90 * 2 * 16 * 48000 / 3200)
# 8
# li = "АКЛМНЯ"
# cnt = 1
# for i in li:
#     for j in li:
#         for k in li:
#             for a in li:
#                 for b in li:
#                     if i == 'К' and j == "М":
#                         print(cnt)
#                     cnt += 1
# print(14 * 21504 / 2 ** 10)
# 12
# for n in range(4, 1000):
#     s = '3' + n * '5'
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '32', 1)
#         if '355' in s:
#             s = s.replace('355', '25', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     if sum(list(map(int, list(s)))) == 17:
#         print(n)
#         break #26
