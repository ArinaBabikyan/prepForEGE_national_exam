a = 56754376
if not a % 2:
    a = a * 4 // 100000
else:
    a = a * 3 // 100000 % 1000
a //= 42
if a > 146:
    print(a // 2)
else:
    print(a // 3)