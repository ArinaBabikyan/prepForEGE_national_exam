with open('26') as f:
    li = f.readlines()
    n = int(li.pop(0))
    li = [list(map(int, i.split())) for i in li]
    li = sorted(li, key=lambda x: x[0])
    rooms = [0 for i in range(20)]
    cnt = 0
    for i in li:
        for j in range(20):
            if i[0] > rooms[j]:
                rooms[j] = 0
        for j in range(20):
            if not rooms[j]:
                rooms[j] = i[0] + i[1]
                break
        else:
            cnt += 1
        print(rooms)
    print(cnt)

