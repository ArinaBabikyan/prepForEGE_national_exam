for i in range(180, -1, -1):
    s = '0' + '3' * i + '2' * (198 - i) + '0'
    while '00' not in s:
        if '011' in s:
            s.replace('011', '201', 1)
        if '03' in s:
            s.replace('03', '220', 1)
        if '02' in s:
            s.replace('02', '210', 1)
        if '012' in s:
            s.replace('012', '2101', 1)
        if '013' in s:
            s.replace('013', '12101', 1)
        if '010' in s:
            s.replace('010', '1100', 1)
    if s.count('1') == 220 and s.count('2') == 197:
        print('0' + '3' * i + '2' * (198 - i) + '0')
        break
