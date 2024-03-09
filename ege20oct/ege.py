#5
"""mi = 1918293892893
mimi= 0
for n in range(1, 10000):
    n2 = bin(n)[2:]
    li = list(str(n2))
    n2 += str(sum(list(map(int, li))) % 2)
    n2 += str(sum(list(map(int, li))) % 2)
    r = int(n2, 2)
    if r > 115:
        mi = min(r, mi)
print(mi)"""
#6
"""import turtle as t

mashtab = 10
n = 100
t.left(90)
for i in range(n):
    t.forward(10 * mashtab)
    t.right(80)
t.up()
input()"""
#12
"""s = '5' * 146
while '333' in s or '555' in s:
    if '555' in s:
        s = s.replace('555', '3', 1)
    elif '333' in s:
        s = s.replace('333', '5', 1)
print(s)"""
#14
"""def p(osn):
    n = 224
    s = []
    for j in range(len(str(n))):
        s.append((int(str(n)[j]) * (osn ** (len(str(n)) - j - 1))))
    s = sum(s)
    return s

cnt = 0
for i in range(5, 11):
    if p(i) + 1 == 65:
        print(i)"""
#15
"""def F(A):
    for x in range(1, 1000):
        if not ((not(x % 6 == 0) or not (x % 14 == 0)) or (x + A >= 70) and (A % 20 == 0)):
            return False
    return True

for A in range(1, 1000):
    if F(A):
        print(A)
        break"""
#16
"""import functools

@functools.lru_cache
def F(n):
    if n <= 1:
        return 2
    else:
        return F(n - 1) + F(n - 2) + 2 * n + 4

print(F(25))"""