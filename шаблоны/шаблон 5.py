"""mi = 1918293892893
for n in range(10000):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
        n2 += bin((n % 3) * 3)[2:]
    r = int(n2, 2)
    if int(n2, 2) > 151:
      mi = min(r, mi)
print(mi)"""
ma = -1
for n in range(10000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = "11" + n2 + "11"
    else:
        n2 = "1" + n2 + "0"
    r = int(n2, 2)
    if int(n2, 2) < 126:
      ma = max(r, ma)
print(ma)