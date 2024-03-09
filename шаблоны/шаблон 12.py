for i in range(1, 1000):
    for j in range(1, 1000):
        s = '1' * i + '3' * j
        while '12' in s or '13' in s:
            if '12' in s:
                s = s.replace('12', '21', 1)
            if '31' in s:
                s = s.replace('31', '23', 1)
            if '13' in s:
                s = s.replace('13', '23', 1)
        if sum(list(map(int, list(s)))) == 404 and '1' not in s:
            print(i + j, i, j)

