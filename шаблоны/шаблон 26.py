with open("26_2024.txt") as file:
    li = list(map(lambda x: list(map(int, x.strip().split())), file.readlines()))[1:]
    li = sorted(li, key=lambda x: [x[1], x[0]])
    x = li[0][1]
    res = [li[0]]
    for i in li[1:]:
        if i[0] >= x:
            x = i[1]
            res.append(i)
ma = 0
x = res[-2][1] #предпоследнее значение
for i in li[::-1]:
    if i[0] - x > ma:
        ma = i[0] - x
print(len(res), ma)