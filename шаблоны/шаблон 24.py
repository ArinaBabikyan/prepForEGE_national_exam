"""with open("24_2024.txt") as file:
    li = [-1]
    ma = 0
    s = file.read().strip()
    s = s.split("T")"""
""" for i in range(len(s)):
        if s[i] == "T":
            li.append(i)
    li.append(len(s))
    for i in range(1, len(li) - 100):
        ma = max(li[i + 100] - li[i - 1] - 1, ma)
    print(ma)"""