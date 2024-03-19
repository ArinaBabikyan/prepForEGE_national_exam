with open('17') as f:
    li = [int(i) for i in f.readlines()]
    ma = max([i for i in li if str(i)[-3:] == '821'])
    mi = min([i for i in li if str(i)[-3:] == '821'])
    key = 2 * (ma + mi)
    cnt = 0
    ma2 = 0
    for i in range(4, len(li)):
        li1 = li[i - 4:i]
        lens = list(map(lambda x: len(str(x)), li1))
        if lens.count(5) > lens.count(3):
            if list(map(lambda x: x % 5, li1)).count(0) == list(map(lambda x: x % 7, li1)).count(0):
                if sum(li1) > key:
                    ma2 = max(sum(li1), ma2)
                    cnt += 1

    print(cnt, ma2)


