# for n in range(1, 10000):
#     t = sum(list(map(int, list(str(n)))))
#     res = ''
#     for i in str(n):
#         if i == '0':
#             res += ''
#         else:
#             res += str(t % int(i))
#     #print(''.join(sorted(res, reverse=True)))
#     r = ''.join(sorted(res, reverse=True))
#     if int(r) > 2000:
#         print(n, r)
#         break

# import turtle as t
# t.up()
# mash = 0.5
# t.left(90)
# t.right(270)
# t.forward(350 * mash)
# t.right(270)
# t.forward(50 * mash)
# t.right(180)
# t.down()
# for i in range(20):
#     t.forward(530 * mash)
#     t.right(90)
#     t.forward(380 * mash)
#     t.right(90)
# t.up()
# t.right(90)
# t.forward(10 * mash)
# t.right(90)
# t.forward(20 * mash)
# t.right(270)
# t.down()
# for i in range(32):
#     t.forward(830 * mash)
#     t.right(270)
#     t.forward(530 * mash)
#     t.right(270)
#
# input()
# print(530 * 380 - 20 * 380 - 510 * 10 + 121 - 1000)
# with open('09_4_1711727598.csv') as f:
#     li = [sorted(list(map(int, i.split(';')))) for i in f.readlines()]
#     li = list(filter(lambda x: x[-2] - 20 == x[1], li))
#     print(len(li), li)
# for n in range(9999, 2, -1):
#     s = '9' + n * '6'
#     while '666' in s or '9909' in s or '66' in s:
#         if '666' in s:
#             s = s.replace('666', '999', 1)
#         if '9909' in s:
#             s = s.replace('9909', '6', 1)
#         if '66' in s:
#              s = s.replace('66', '0', 1)
#     if len(s) == 10:
#         print(n, s)
#         break

print(bin(224)[2:].zfill(8) + '.' + '0' * 8)
print(8 * 2 + 3)
print()
print(bin(192)[2:].count('1') + bin(168)[2:].count('1') + bin(160)[2:].count('1'))

# ma = 0
# res = 0
# for x in range(22):
#     for y in range(22):
#         if (int(f'34256{x}4', 22) + int(f'72847{y}3', 22)) % 125 == 0:
#             if  (x+y > ma):
#                 ma = x+y
#                 res = (int(f'34256{x}4', 22) + int(f'72847{y}3', 22)) / 125
# print(res)


# def f(A):
#     for x in range(1, 10000):
#         if not (not x % 72 == 0 or x % 495 == 0 or not x % A == 0):
#             return False
#     return True
#
# for a in range(1, 100):
#     if f(a):
#         print(a)
# with open('17_prob') as f:
#     li = [int(i) for i in f.readlines()]
#     mi = max(li)
#     for i in li:
#         if mi > i and i > 0 and len(str(i)) == 2:
#             mi = i
#
#     cnt = 0
#     mi = str(mi)
#     mi2 = 10 ** 100
#     for i in range(1, len(li)):
#         a, b = li[i - 1], li[i]
#         if mi in str(a) and mi in str(b):
#             continue
#         cnt += 1
#         mi2 = min(mi2, abs(a - b))
#     print(cnt, mi2)