# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             print(x, y, z, (not y or x) and (not x or z))
# 5'
# cnt = 0
# for i in range(1000, 9999):
#     new = sorted([(i // 1000) * ((i % 1000) // 100), ((i % 1000) // 100) * ((i % 100) // 10), ((i % 100) // 10) * (i % 10)], reverse=True)
#     new = ''.join(list(map(str, new)))
#     if new == "12106":
#         cnt += 1
#         print(i)
# print(cnt)
# 6
# import turtle as t
# t.left(90)
# mash = 5
#
# t.speed(1000)
# for i in range(10):
#     t.forward(50 * mash)
#     t.right(90)
# t.up()
# for x in range(50):
#     for y in range(50):
#         t.goto(x * mash, y * mash)
#         t.dot(3)
# input()
#print(eval("1488 * 1337 * x <= 3 * 2 ** 23"))
# диана
# print(5 * 4 * 3 * 2 - 4 * 4)

# with open('9.prob') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     cnt = 0
#     for i in li:
#         a = sorted(i)
#         if a[0] * a[4] * 3 > sum(a[1:4]) ** 2:
#             cnt += 1
#             print(a)
#     print(cnt)

# 13
# cnt = 0
# for i in range(0, 256):
#     if bin(i)[2:].count('1') != 4:
#         print(bin(i)[2:])
#         cnt += 1
# print(cnt)

#14
# s = (2 ** 8 * 2 ** 4 * 17333263511920313 * 4 + 2 ** 8)
# res = ''
# while s > 0:
#     s //= 111
#     res += str(s % 111)
# print(res)

# 15
# def f(a, b):
#     for x in range(1000):
#         if not ( (not (10 <= x <= 33) or (a <= x <= b)) or (40 <= x <= 45)):
#             return False
#     return True
# mi = 1000
# for a in range(1000):
#     for b in range(a, 1000):
#         if f(a, b):
#             mi = min(b - a, mi)
#             if mi == 23:
#                 print(a, b)
#                 break
# print(mi)
# 16
# def F(n):
#     if n < 3:
#         return 2
#     if n % 2 == 0:
#         return 2 * F(n - 2) - F(n - 1) + 2
#     return 2 * F(n - 1) - F(n - 2) - 2
#
# print(F(24))
# 17
# with open('17.prob.march.08.py') as f:
#     li = [int(i) for i in f.readlines()]
#     ma = -10 ** 10
#     cnt = 0
#     for i in range(1, len(li)):
#         su = abs(li[i - 1] + li[i])
#         k = ''
#         k += str(su % 5)
#         su //= 5
#         k += str(su % 5)
#         su //= 5
#         if k == '41' and str(li[i - 1]).count('3') == 2:
#             cnt += 1
#             print(li[i - 1] + li[i], k)
#             ma = max(ma, li[i - 1] + li[i])
#     print(cnt, ma)
# 23
# def ways(s, f):
#     if s == f:
#         return 1
#     if s == 35 or s > f:
#         return 0
#     first = s // 10
#     print(s, first, (first + int(bool(10 - first - 1))) * 10 + s % 10)
#     return ways(s + 5, f) + ways((first + int(bool(10 - first - 1))) * 10 + s % 10, f)
#
# print(ways(30, 60))
# 24
# with open('24.prob.08march') as f:
#     # for i in (f.readline().split('A')):
#     #     if len(i) == 28:
#     #         print(i)
#     ma = max(list(map(lambda x: len(x), f.readline().split('A'))))
#     print(ma)
# 26
# with open('26.prob.08march') as f:
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     n, m = li.pop(0)
#     gr = sorted(list(map(lambda x: (x[1] / x[0], x[0]), li)), key=lambda x: (x[0], -x[1]))
#     li1 = (gr[:m])
#     print(li1)
#     print(sum(list(map(lambda x: x[1], li1))))
#     print(max(li1, key=lambda x: x[1]))
#     print(438)
# 27
# with open('27.prob.08march') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     w = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if (li[i] * li[j]) % 49 and not (li[i] * li[j]) % 7:
#                 w = max(w, li[i] * li[j])
#     print(w)
# file = open('27.prob.08march')  # считываем файл с данными
# n = int(file.readline())  # считываем количество чисел n
#
# c7 = 0  # создаём переменную, где будем хранить максимальное число, кратное 7, но не кратное 49
# c = 0  # и переменную для хранения максимального числа, не кратного 7 и 49
#
# for i in range(n):  # проходимся по всему файлу
#     x = int(file.readline())  # считываем текущее число
#
#     # если х кратен 7, но не 49, проверяем, является ли он максимальным
#     # и если да, то сохраняем в с7
#     if x % 7 == 0 and x % 49 != 0:
#         c7 = max(x, c7)
#     # аналогичная проверка для х, не кратного ни 7, ни 49
#     elif x % 49 != 0:
#         c = max(x, c)
#
# # находим итоговое W
# W = c*c7
#
# # eсли произведение получить невозможно, считается,
# # что контрольное значение W = 1 - это произойдет в случае, если с7 = 0 или с = 0
# if W == 0:
#     W = 1
# print(W)  # выводим ответ
