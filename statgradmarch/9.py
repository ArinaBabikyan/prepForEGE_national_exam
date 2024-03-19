with open('9') as f:
    li = [list(map(int, i.split())) for i in f.readlines()]
    cnt = 0
    int = []
    for i in range(len(li)):
        if len(set(li[i])) == len(li[i]):
            for j in range(6):
                li1 = [li[m][j] for m in range(i, len(li))]
                if li1.count(li[i][j]) > 140:
                    int.append(li[i][j])

    cnt2 = 0
    for i in li:
        cnt = 0
        for j in i:
            if j in int:
                cnt += 1
        if cnt >= 3:
            if len(set(i)) == len(i):
                cnt2 += 1
    print(cnt2)
