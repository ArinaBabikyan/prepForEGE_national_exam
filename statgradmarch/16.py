import functools
@functools.cache
def F(a, b):
    if b == 0:
        return 0
    if b > 0 and not b % 2:
        return 2 * F(a, b / 2)
    return a + F(a, b - 1)

for x in range(1000000):
    for y in range(1000000, x, -1):
        if F(x, y) == 89999:
            print(y)
            break