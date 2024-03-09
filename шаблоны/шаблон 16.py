import functools

@functools.lru_cache
def F(n):
    if n <= 3:
        return n
    else:
        if n % 2:
            return F(n - 1) * F(n - 3)
        return F(n - 1) + 2 * F(n / 2)

for i in range(1, 1000):
    if F(i) <= 10 ** 8:
        print(i)