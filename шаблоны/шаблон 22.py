def toposort(a):
    b = [] # пустой список b
    used = {0} # множество посещенных процессов (0 - псевдо для независимых)
    while len(b) < len(a): # пока все процессы не посещены
        for i in range(len(a)): # перебор всех процессов
            if a[i][0] not in used and set(a[i][2:]) <= used: # если процесс не
                # посещен и все влияющие на него процессы посещены
                b.append(a[i]) # добавляем процесс в список b
                used.add(a[i][0]) # добавляем ID процесса в множество посещенных
    return b # возвращаем заполненный список b

s  = open('22-27.csv').read().strip()[:-1]
s = s.replace('"', '').replace(';;', ';').replace(';\n', '\n')
a = s.split('\n')[1:]
for i in range(len(a)):
    a[i] = list(map(int, a[i].split(';')))
a = toposort(a) # заменяем список a на сортированный список b
for i in range(len(a)):
    if len(a[i]) > 2 and a[i][2] != 0:
        for k in range(2, len(a[i])):
            for j in range(i):
                if a[i][k] == a[j][0]:
                    a[i][k] = a[j][1]
                    break
        a[i][1] += max(a[i][2:])
print(max(a, key=lambda x: x[1])[1])

