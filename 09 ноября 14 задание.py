ma = -1
for x in range(0, 37):
    for y in range(0, 37):
        if (2 * 37 ** 7 + 37 ** 6 + x * 37 ** 5 + 4 * 37 ** 4 + 5 * 37 ** 3 + 7 * 37**2 + y + 9) % 36 == 0:
            ma = max(ma, x * 37 + y)
print(ma)