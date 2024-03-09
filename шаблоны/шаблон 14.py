"""ma = -1
print(int('A9', 16))
for i in '0123456789ABCDEFGHI':
    if (int('9897' + i + '21', 19) + int('2' + i + '923', 19)) % 18 == 0:
        print(i, (int('9897' + i + '21', 19) + int('2' + i + '923', 19)) // 18)"""
"""n = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
s = []
while n > 0:
    s.append(n % 25)
    n //= 25
print(s.count(0))
""""""
def p(osn):
    n = 611
    s = []
    while n > 0:
        s.append(n % osn)
        n //= osn
    s = s[::-1]
    s = list(map(str, s))
    s = int(''.join(s))
    print(s, (len(str(s))), osn)
    if (len(str(s))) % 2:
        return n
    return 0

cnt = 0
for i in range(2, 11):
    cnt += p(i)
    print(cnt)
print(cnt)"""