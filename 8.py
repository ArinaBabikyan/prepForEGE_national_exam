# import itertools
# cnt = 0
# li = []
# for i in itertools.permutations('одеколон', 8):
#     s = ''.join([j for j in i])
#     if 'оо' not in s and s not in li:
#         print(s)
#         li.append(s)
#         cnt += 1
# print(cnt)
cnt = 1
li = ["А", "К", "Р", "У"]
for i in li:
    for j in li:
        for k in li:
            for z in li:
                for m in li:
                    if i + j + k + z + m == "УКАРА":
                        print(cnt)
                    cnt += 1
                    #print(i + j + k + z + m)