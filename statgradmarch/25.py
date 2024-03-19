with open('25') as f:
    li = f.readline()
    ma = 0
    print(li.count("X"), li.count("Y"))
    for i in range(len(li)):
        for j in range(len(li), i, -1):
            if li[i:j].count('X') == li[i:j].count('Y'):
                print(j - i)
                break