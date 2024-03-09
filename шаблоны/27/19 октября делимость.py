with open("inf_22_10_20_27b.txt") as f:
    li = f.readlines()
    li.pop(0)
    li1 = [abs(int(i.split(" ")[0]) - int(i.split(" ")[1])) for i in li]
    for i in range(len(li1)):
        