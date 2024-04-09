# with open('26-2.txt') as f:
#     n = int(f.readline())
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     li = sorted(li, key=lambda x: x[0])
#     queue1 = []
#     queue2 = []
#     cnt = 0
#     cnt1 = 0
#     for i in li:
#         queue1 = list(filter(lambda x: x > i[0], queue1))
#         queue2 = list(filter(lambda x: x > i[0], queue2))
#         if i[2] == 0:
#             if len(queue1) < len(queue2):
#                 i[2] = 1
#             elif len(queue1) > len(queue2):
#                 i[2] = 2
#             elif len(queue1) < 12:
#                 i[2] = 1
#             elif len(queue1) < 12:
#                 i[2] = 2
#             else:
#                 cnt += 1
#                 continue
#         if i[2] == 1:
#             if not queue1:
#                 queue1.append(i[0] + i[1])
#                 cnt1 += 1
#             else:
#                 if len(queue1) < 12:
#                     queue1.append(queue1[-1] + i[1])
#                     cnt1 += 1
#                 else:
#                     cnt += 1
#         elif i[2] == 2:
#             if not queue2:
#                 queue2.append(i[0] + i[1])
#             else:
#                 if len(queue2) < 12:
#                     queue2.append(queue2[-1] + i[1])
#                 else:
#                     cnt += 1
#
#     print(cnt1, cnt)

#
# with open('26-2.txt') as f:
#     n = int(f.readline())
#     li = [list(map(int, i.split())) for i in f.readlines()]
#     queue1 = []
#     queue2 = []
#     cnt = 0
#     for i in li:
#         queue1 = list(filter(lambda x: x < i[2], queue1))
#         queue2 = list(filter(lambda x: x < i[2], queue2))
#         if i[2] == 0:
#             if len(queue1) < len(queue2):
#                 if len(queue1) < 14:
#                     i[2] = 1
#                 else:
#                     cnt += 1
#             elif len(queue1) > len(queue2):
#                 if len(queue2) < 14:
#                     i[2] = 2
#                 else:
#                     cnt += 1
#             elif len(queue1) < 14:
#                 i[2] = 1
#             elif len(queu1) < 14:
#                 i[2] = 2
#             else:
#                 cnt += 1
#                 continue
#         if i[2] == 1:
#             if not queue1:
#                 queue1.append(i[0] + i[1])
#             else:
#                 if len(queue1) < 14:
#                     queue1.append(queue1[-1] + i[1])
#                 else:
#                     cnt += 1
#         if i[2] == 2:
#             if not queue2:
#                 queue2.append(i[0] + i[1])
#             else:
#                 if len(queue2) < 14:
#                     queue2.append(queue2[-1] + i[1])
#                 else:
#                     cnt += 1
#     print(cnt)
with open('26-3.txt') as f:
    n = int(f.readline())
    li = sorted([int(i) for i in f.readlines()], reverse=True)
    containers = []
    counts = []
    for i in range(n):
        if containers:
            for j in range(len(containers)):
                if li[i] + 7 <= containers[j]:
                    containers[j] = li[i]
                    counts[j] += 1
                    break
            else:
                containers.append(li[i])
                counts.append(1)
        else:
            containers.append(li[i])
            counts.append(1)
    print(len(containers), max(counts))
