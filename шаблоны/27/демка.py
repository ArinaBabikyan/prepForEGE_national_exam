"""with open("27_A_2024.txt") as file:
    li = list(map(int, file.readlines()))
    k = int(li.pop(0))
    n = int(li.pop(0))
    ma = 0
    for i in range(n - 2 * k):
        for j in range(i + k, n - k):
            for z in range(j + k, n):
                ma = max(ma, li[i] + li[j] + li[k])
print(ma)"""
"""with open("27-B (5).txt") as file:
    li = list(map(int, file.readlines()))
    n = (li.pop(0))
    k = 18
    ma = 0
    superma = 0
    no = 0
    for i in range(k, n):
        if (li[i - k] + li[i]) % 8 == 0 and li[i - k] * li[i] % 2187 == 0:
            no += 1
            print(li[i - k], li[i])
print(no)"""
def count3(k):
    if k % 3 != 0:
        return 0
    return min(7, count3(k // 3) + 1)

n = 0
a = []
with open("27-B (5).txt", "r") as f:
    n = int(f.readline())
    for i in range(n):
        a.append(int(f.readline()))

lm = []
for i in range(8):
    rm = []
    for j in range(8):
        rm.append(0)
    lm.append(rm)

count = 0
for i in range(18, n):
    lm[a[i - 18] % 8][count3(a[i - 18])] += 1
    x = count3(a[i])
    for j in range(x + 1):
        count += lm[(8 - (a[i] % 8)) % 8][7 - j]
print(count)