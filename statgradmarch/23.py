li = [(0, 215),
(0, 272),
(272, 539),
(539, 763),
(539, 832),
(832, 984),
(0, 193),
(0, 222),
(-222,672),
(672, 763),
(763, 1003),
(672, 982),
(763, 1043),
(1003, 1177)]
count = 0
res = []
for i in range(1177):
    cnt = 0
    for j in li:
        #print(j[0], j[1])
        if j[1] > i and j[0] < i:
            cnt += 1
    if cnt == 5:
        count += 1
    else:
        res.append(count)
        count = 0
print(res)