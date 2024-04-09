# номер 1
# with open('27.1-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     #ost = [i % 80 for i in li]
#     ma = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if abs(li[j] - li[i]) % 80 == 0:
#                 ma = max(ma, abs(li[j] - li[i]))
#     print(ma)
# with open('27.1-B') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     ost = [[] for i in range(n)]
#     res = 0
#     for i in range(n):
#         x = li[i]
#         for j in ost[x % 80]:
#             res = max(res, abs(x - j))
#         ost[x % 80].append(x)
#     print(res)
# номер 2
# with open('27.2-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     cnt = 0
#     for i in range(n):
#         for j in range(i + 6, n):
#             if (li[i] - li[j]) % 13 == 0 and (li[i] * li[j]) % 2 == 0:
#                 cnt += 1
#     print(cnt)
# with open('27.2-B') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     cnt = 0
#     ost = [[] for i in range(13)]
#     res = 0
#     temp = []
#     for i in range(6, n):
#         x = li[i]
#         a = li[i - 6]
#         ost[a % 13].append(a)
#         #print(x % 13, [i % 13 for i in ost[x % 13]])
#         for j in ost[x % 13]:
#             if (x * j) % 2 == 0:
#                 res += 1
#                 #print(x, j, x%13, j % 13)
#     print(res)
# номер 3
# with open('27.3-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     k = li.pop(0)
#     res = 0
#     for i in range(n - 1):
#         for j in range(i + 1, i + 1 + k):
#             if j < n:
#                 if (li[i] + li[j]) % 17 == 0:
#                     res += 1
#     print(res)
#     # count = 0
#     # a = li
#     # for i in range(n - 1):
#     #     for j in range(i + 1, n):
#     #         # Проверяем, что разница номеров элементов меньше или равна k, а их сумма кратна 17
#     #         if j - i <= k and (a[i] + a[j]) % 17 == 0:
#     #             count += 1  # И увеличиваем количество подходящих пар
#     # print(count)
# with open('27.3-B') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     k = li.pop(0)
#     ost = [[] for i in range(17)]
#     res = 0
#     for i in range(n):
#         x = li[i]
#         for j in ost[-x % 17]:
#             res += 1
#         ost[x % 17].append(x)
#         if i >= k:
#             ost[li[i - k] % 17].remove(li[i - k])
#     print(res)
# номер 4
# with open('27.4-A') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     k = li.pop(0)
#     ost = [[] for i in range(2023)]
#     ma = 0
#     par = ()
#     res = 0
#     for i in range(n):
#         for j in range(i + k, n):
#             if (li[i] + li[j]) % 2023 == 0:
#                 if (li[i] % 47 == 0) != (li[j] % 47 == 0):
#                     ma = max(ma, li[i] + li[j])
#                     if ma == li[i] + li[j]:
#                         par = (li[i], li[j])
#                     res += 1
#     print(ma, par, res)
# with open('27.3-B') as f:
#     li = [int(i) for i in f.readlines()]
#     n = li.pop(0)
#     k = li.pop(0)
#     ost = [[] for i in range(2023)]
#     res = 0
#     ma = 0
#     par = ()
#     for i in range(k, n):
#         x = li[i]
#         a = li[i - k]
#         ost[a % 2023].append(a)
#         for j in ost[-x % 2023]:
#             if (x % 47 == 0) != (j % 47 == 0):
#                 if ma < x + j:
#                     ma = x + j
#                     par = (x, j)
#                 res += 1
#     print(ma)
# задача 5
# with open('27.5-A') as f:
#     li = [int(i) for i in f.readlines()]
#     k = li.pop(0)
#     n = li.pop(0)
#     mi = 10 ** 30
#     for i in range(n - 2 * k):
#         for j in range(i + k, n - k):
#             for z in range(j + k, n):
#                 mi = min(mi, li[i] + li[j] + li[z])
#     print(mi)
# Эффективное
# with open('27.6-B') as f:
#     li = [int(i) for i in f.readlines()]
#     k = li.pop(0)
#     n = li.pop(0)
#     mi = 10 ** 30
#     mi1 = 10 ** 30
#     mi2 = 10 ** 30
#     for i in range(n - 2 * k):
#         mi = min(mi, li[i])
#         mi1 = min(mi1, mi + li[i + k])
#         mi2 = min(mi2, mi1 + li[i + 2 * k])
#     print(mi2)
# задача 6
# with open('27.6-A') as f:
#     li = [int(i) for i in f.readlines()]
#     k = li.pop(0)
#     n = li.pop(0)
#     ma = 0
#     for i in range(n):
#         for j in range(i + k, n, k):
#             ma = max(ma, li[i] * li[j])
#     print(ma)
#
#
#
# with open('/Users/arishababikyan/Downloads/172820b9-06c3-4af4-980e-3b4b981631f5.txt') as f:
# #with open('27.6-A') as f:
#     li = [int(i) for i in f.readlines()]
#     k = li.pop(0)
#     n = li.pop(0)
#
#     ma1 = 0
#     for i in range(k):
#         ma = 0
#         for j in range(i, n, k):
#             ma1 = max(ma1, li[j] * ma)
#             ma = max(li[j], ma)
#     print(ma1)
#
#
# f = open('27_B.txt')  # открываем файл
# k = int(f.readline())  # считываем число k
# n = int(f.readline())  # считываем число n
# a = [int(x) for x in f]  # считываем числа из файла
# max_chisla = [-10 ** 19] * k  # создаём список из k элементов, в который будем записывать максимальные числа на определенном расстоянии от рассматриваемого
# # к примеру, k = 3, у первого числа индекс 10, а у второго 22, 22-10=12, число кратно k, так как оба числа при делении на 3 получают остаток 1, поэтому
# # если индексы двух чисел будут иметь одинаковый остаток, то расстояние между ними будет кратно числу k
# min_chisla = [10 ** 20] * k  # так как в файле есть отрицательные числа, то по такому же принципу будем фиксировать минимальные числа
# max_res = -10 ** 19  # создаём переменную, в которую будем записывать максимальное значение
# for x in range(k, len(a)):  # начинаем перебор с k, то есть с минимального возможного расстояния между числами
#     max_chisla[x % k] = max(max_chisla[x % k], a[x - k])  # в обоих списках меняем числа на максимальное и минимальное, обращаясь по остатку от деления
#     # индекса x на число k и при необходимости меняем на число a[x-k], то есть на то, которое находится на расстоянии k от рассматриваемого
#     min_chisla[x % k] = min(min_chisla[x % k], a[x - k])
#     max_res = max(max_res, max_chisla[x % k] * a[x], min_chisla[x % k] * a[x])  # умножаем рассматриваемое число на максимальное и минимальное, имеющие такие же остатки
#     # максимальное из результатов записываем в max_res
# print(max_res)  # выводим максимальное значение

# задачи на группы чисел