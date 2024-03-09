cnt = 0
for d1 in 'КАБАЛА':
    for d2 in 'КАБАЛА':
        for d3 in 'КАБАЛА':
            for d4 in 'КАБАЛА':
                for d5 in 'КАБАЛА':
                    s = d1 + d2 + d3 + d4 + d5
                    if "АА" not in s:
                        cnt += 1
print(cnt)