# def f(A):
#     for x in range(100):
#         if not(not (x & 57665 == 0) or (not (x & 83265 != 0) or (x & A) != 0)):
#             return False
#     return True
#
# cnt = 0
# for i in range(1, 2 ** 20):
#     if f(i):
#         cnt += 1
# print(cnt)
a = (bin(90753)[2:])
print(a)
s = ''
for i in a:
    if i == '1':
        s += '0'
    else:
        s += '1'
print(s)
s = (len(bin(2 ** 20)[2:]) - len(s)) * '0' + s
print(s)
print('0' + (bin(57476)[2:]))
for i in range(len(s)):
    if s & 57476
    if s[i] == '1':
