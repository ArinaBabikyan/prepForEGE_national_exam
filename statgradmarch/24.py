def ways(s, f, cnt):
    if s == f:
        return 1
    if s > f or cnt > 4:
        return 0

    return ways(s + 1, f, cnt + (not (s + 1) % 2)) + ways(s * 2, f, cnt + 1)

print(ways(1, 17, 0))