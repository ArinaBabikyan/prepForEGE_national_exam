"""print('z, w, y, x, f')
for x in [0, 1]:
    for y in [0, 1]:
        for w in [0,1]:
            for z in [0, 1]:
                f = not (w or x or y) or ((y or z) and x or y and (w or z))
                if f == 0:
                    print(y, w, z, x, f)"""

"""cnt = 0
for n in range(1000000000):
    x = sum([int(i) for i in (str(n))])
    x = bin(x)[2:]
    if x.count('1') % 2 == 0:
        x = '1' + x + '00'
    else:
        x = '10' + x + '1'
    r = int(x, 2)
    if int(r) == 21:
        print(n, r)
        cnt += 1
    if n == 2:
        print(r)
print(cnt)"""
'''/Users/arishababikyan/PycharmProjects/mybabyEGE/venv/bin/python "/Users/arishababikyan/PycharmProjects/mybabyEGE/probnik 30.01.py"
2 21
21
11 21
20 21
101 21
110 21
200 21
1001 21
1010 21
1100 21
2000 21
10001 21
10010 21
10100 21
11000 21
20000 21
100001 21
100010 21
100100 21
101000 21
110000 21
200000 21
1000001 21
1000010 21
1000100 21
1001000 21
1010000 21
1100000 21
2000000 21
10000001 21
10000010 21
10000100 21
10001000 21
10010000 21
10100000 21
11000000 21
20000000 21
100000001 21
100000010 21
100000100 21
100001000 21
100010000 21
100100000 21
101000000 21
110000000 21
200000000 21
'''

print(8000 / 60)