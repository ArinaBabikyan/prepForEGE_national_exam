with open('17-1.txt') as f:
    ma = -99999999
    n = 0
    li = list(map(int, f.readlines()))
    sr = sum(li) / len(li)
    for i in li:
        if i % 17 == 0 and i > sr:
            n += 1
            if i > ma and i != max(li):
                ma = i
        elif i % 17 == 0:
            n += 1
            if i > ma and i != max(li):
                ma = i
        elif i > sr:
            n += 1
            if i > ma and i != max(li):
                ma = i
    print(n * (len(li) - 1))
    print(ma+max(li))