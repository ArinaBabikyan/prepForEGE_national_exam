cnt = 0
for i in range(1000000000, 10000000000):
    s = str(i)
    if s[-1] in s[:len(s)]:
        cnt += 1
print(cnt)