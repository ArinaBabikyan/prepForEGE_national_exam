# def troich(n):
#     if n == 0:
#         return '0'
#     s = ''
#     while n > 0:
#         s += str(n % 3)
#         n //= 3
#     return s[::-1]
# for i in range(19000, 1, -1):
#     k = troich(i)
#     k += troich(k.count('2'))
#     k += troich(k.count('1'))
#     k += troich(k.count('0'))
#     if int(k, 3) < 1000:
#         print(i)
#         break
#

# import turtle
# turtle.left(90)
# mash = 50
# for i in range(36):
#     turtle.forward(1 * mash)
#     turtle.right(36)
# turtle.up()
# turtle.forward(4 * mash)
# turtle.right(90)
# turtle.down()
# for i in range(8):
#     turtle.forward(6 * mash)
#     turtle.right(90)
# turtle.up()
# turtle.goto(0,0)
# for x in range(10):
#     for y in range(5):
#         turtle.goto(x * mash, y * mash)
#         turtle.dot(5)
# turtle.goto(0,0)
# for x in range(10):
#     for y in range(5):
#         turtle.goto(x * mash, -y * mash)
#         turtle.dot(5)
# input()
# print(8.27 * 11.69* 600 * 8 * 10 * 600/ (2 ** 23))
import functools
import math
@functools.cache
def rec(decoded, s_part):
    global di, li
    if not s_part and decoded and decoded not in li:
        li.append(decoded)
        return 1
    if len(s_part) == 2 and s_part in di.keys():
        return rec(decoded + di[s_part[:2]], '') + rec(decoded + di[s_part[:1]], s_part[1:])
    if len(s_part) == 1:
        return rec(decoded + di[s_part[:1]], '')
    if s_part[:2] in di.keys() and s_part[:1] in di.keys():
        return rec(decoded + di[s_part[:2]], s_part[2:]) + rec(decoded + di[s_part[:1]], s_part[1:])
    if s_part[:2] in di.keys():
        return rec(decoded + di[s_part[:2]], s_part[2:])
    if s_part[:1] in di.keys():
        return rec(decoded + di[s_part[:1]], s_part[1:])
    return 0

with open('27_A.txt') as f:
    alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩъЫьЭЮЯ '
    di = {}
    cnt = 1
    for i in alph:
        di[str(cnt)] = i
        cnt += 1
    s = f.readline()
    res = 1
    decoded = []
    f = False
    cnt2 = 0
    for i in range(1, len(s)):
        if (s[i - 1:i + 1]) in di.keys() and s[i] != '0':
            if f:
                cnt2 += res
                print(i, s[i - 1:i + 1], s[i - 2:i], res)
            f = True
            res *= 2
        else:
            f = False

    print(res - cnt2)
