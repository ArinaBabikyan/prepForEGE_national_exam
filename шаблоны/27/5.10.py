with open("28129_B (2).txt") as f:
    li = f.readlines()
    li1 = [0 for i in range(160)]
    print(li1)
    for i in li:
        li1[int(i) % 160] = max(int(i), int(li[int(i) % 160]))

