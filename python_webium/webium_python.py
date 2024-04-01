li = [26, 22, 25, 111, 49, 35, 137, 133, 46, 61]
res = li.copy()
for i in range(1, len(li)):
    res[i] = sum(li[:i + 1]) / (i + 1)
print(li)
print(res)
print(sum(res) // len(res))