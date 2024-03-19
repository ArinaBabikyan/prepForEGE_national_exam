# print(30 * 2 ** 23 / (2 * 32000 * 16 * 0.6))
# t = 409.6
# print(t * 4 * 48000 * 24 / (2 ** 23))
# print(180 / 225)
# print(463-17)
# print(bin(208)[2:])
# print(bin(54)[2:])
# print(7)

import re
for n in range(9517, 10 ** 9, 9517):
    if re.fullmatch('2.{0,50}41.{0,50}6.{1}9', str(n)):
        print(n)