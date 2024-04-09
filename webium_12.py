# 1

# s = 150 * '5'
# while '5555' in s:
#     s = s.replace('5555', '33', 1)
#     if '333' in s:
#         s = s.replace('333', '5', 1)
# print(s)

# 2

# s = '5' * 193
# while '333' in s or '555' in s:
#     if '555' in s:
#         s = s.replace('555', '3', 1)
#     elif '333' in s:
#         s = s.replace('333', '5', 1)
# print(s)


# 3

# s = '2' * 3 + 18 * '5'
# while '222' in s or '888' in s:
#     while '555' in s:
#         s = s.replace('555', '8', 1)
#     if '222' in s:
#         s = s.replace('222', '8', 1)
#     elif '888' in s:
#         s = s.replace('888', '2', 1)
#
# print(s)

# 4

# s = '3' + 57 * '5'
# while '25' in s or '355' in s or '4555' in s:
#     if '25' in s:
#         s = s.replace('25', '3', 1)
#     if '355' in s:
#         s = s.replace('355', '4', 1)
#     if '4555' in s:
#         s = s.replace('4555', '2', 1)
# print(s)

# 5

# s = 120 * '7'
# while '8887' in s or '77' in s:
#     if '8887' in s:
#         s = s.replace('8887', '8', 1)
#     elif '77' in s:
#         s = s.replace('77', '8', 1)
# print(s)

# 6

# s = 52 * 'AB'
# while 'AA' in s or 'BB' in s or 'AB' in s:
#     if 'AA' in s:
#         s = s.replace('AA', 'B', 1)
#     if 'BB' in s:
#         s = s.replace('BB', "A", 1)
#     if 'AB' in s:
#         s = s.replace('AB', 'BA', 1)
# print(s)


# 1 cложные
# s = '6' * 79
# while '666' in s or '2222' in s:
#     if '2222' in s:
#         s = s.replace('2222', '6', 1)
#     elif '666' in s:
#         s = s.replace('666', '2', 1)
# print(s)


# 2
# s = '>' + 11 * '1' + '2' * 12 + '3' * 30
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '222>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>', 1)
# print(sum(list(map(int, s.replace('>', '')))))
# 3
# li = []
# for i in range(1, 1000):
#     s = '1' * i
#     while '1111' in s or '222' in s or '33' in s:
#         if '1111' in s:
#             s = s.replace('1111', '333', 1)
#         elif '222' in s:
#             s = s.replace('222', '11', 1)
#         elif '33' in s:
#             s = s.replace('33', '2', 1)
#     li.append(s)
# print(len(set(li)))

# 4
# for i in range(1, 100):
#     s = '0' * i + '1'
#     while '01' in s:
#         if '1':
#             s = s.replace('1', '10', 1)
#         if '01' in s:
#             s = s.replace('01', '1000', 1)
#     if 999 >= s.count('0') >= 100:
#         print(i)
#         break

# 6
ma = 0
for i in range(204):
    s = '1' * i + '2' + (203 - i) * '1'
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        elif '222' in s:
            s = s.replace('222', '11', 1)
    ma = max(ma, len(s))
print(ma)