cnt = 0
with open('09 ноября задание 9.txt', encoding='utf-8-sig') as f:
    for i in f:
        li = list(map(int, i.strip().split(';')))
        if len(set(li)) == len(li):
            if (min(li) + max(li)) / 2 > (sum(li) - min(li) - max(li)) / 4:
                cnt += 1
print(cnt)